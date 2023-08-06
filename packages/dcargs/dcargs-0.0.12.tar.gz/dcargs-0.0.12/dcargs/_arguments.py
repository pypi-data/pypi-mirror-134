import argparse
import collections.abc
import dataclasses
import enum
from typing import Any, Callable, Dict, List, Optional, Set, Tuple, Type, TypeVar, Union

from typing_extensions import Final, Literal, _AnnotatedAlias, get_args, get_origin

from . import _construction, _docstrings, _strings

T = TypeVar("T")


def _instance_from_string(typ: Type[T], arg: str) -> T:
    """Given a type and and a string from the command-line, reconstruct an object. Not
    intended to deal with generic types or containers; these are handled in the
    "argument transformations" below.

    This is intended to replace all calls to `type(string)`, which can cause unexpected
    behavior. As an example, note that the following argparse code will always print
    `True`, because `bool("True") == bool("False") == bool("0") == True`.
    ```
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("--flag", type=bool)

    print(parser.parse_args().flag)
    ```
    """
    if typ is bool:
        return _strings.bool_from_string(arg)  # type: ignore
    else:
        return typ(arg)  # type: ignore


@dataclasses.dataclass(frozen=True)
class ArgumentDefinition:
    """Options for defining arguments. Contains all necessary arguments for argparse's
    add_argument() method."""

    # Fields that will be populated initially.
    name: str
    field: dataclasses.Field
    parent_class: Type
    type: Optional[Union[Type, TypeVar]]

    # Fields that will be handled by argument transformations.
    required: Optional[bool] = None
    action: Optional[str] = None
    nargs: Optional[Union[int, str]] = None
    default: Optional[Any] = None
    choices: Optional[Set[Any]] = None
    metavar: Optional[Union[str, Tuple[str, ...]]] = None
    help: Optional[str] = None
    dest: Optional[str] = None

    def add_argument(
        self, parser: Union[argparse.ArgumentParser, argparse._ArgumentGroup]
    ) -> None:
        """Add a defined argument to a parser."""
        kwargs = {k: v for k, v in vars(self).items() if v is not None}
        name = "--" + kwargs.pop("name").replace("_", "-")
        kwargs.pop("field")
        kwargs.pop("parent_class")

        # Wrap the raw type with handling for special types. (currently only booleans)
        # This feels a like a bit of band-aid; in the future, we may want to always set
        # the argparse type to str and fold this logic into a more general version of
        # what we currently call the "field role" (callables used for reconstructing
        # lists, tuples, sets, etc).
        if "type" in kwargs:
            raw_type = kwargs["type"]
            kwargs["type"] = lambda arg: _instance_from_string(raw_type, arg)

        parser.add_argument(name, **kwargs)

    def prefix(self, prefix: str) -> "ArgumentDefinition":
        """Prefix an argument's name and destination. Used for nested dataclasses."""
        _strings.NESTED_DATACLASS_DELIMETER
        arg = self
        arg = dataclasses.replace(arg, name=prefix + arg.name)
        if arg.dest is not None:
            arg = dataclasses.replace(arg, dest=prefix + arg.dest)
        return arg

    @staticmethod
    def make_from_field(
        parent_class: Type,
        field: dataclasses.Field,
        type_from_typevar: Dict[TypeVar, Type],
        default_override: Optional[Any],
    ) -> Tuple["ArgumentDefinition", _construction.FieldRole]:
        """Create an argument definition from a field. Also returns a field role, which
        specifies special instructions for reconstruction."""

        assert field.init, "Field must be in class constructor"

        # Create initial argument.
        arg = ArgumentDefinition(
            name=field.name,
            field=field,
            parent_class=parent_class,
            type=field.type,
            default=default_override,
        )

        # Propagate argument through transforms until stable.
        prev_arg = arg
        role: _construction.FieldRole = _construction.FieldRoleEnum.VANILLA_FIELD

        def _handle_generics(arg: ArgumentDefinition) -> _ArgumentTransformOutput:
            """Handle generic arguments. Note that this needs to be a transform -- if we
            only checked field.type before running transforms, we wouldn't be able to
            handle cases like Optional[T]."""
            if isinstance(arg.type, TypeVar):
                assert arg.type in type_from_typevar, "TypeVar not bounded"
                return (
                    dataclasses.replace(
                        arg, type=type_from_typevar[arg.type]  # type:ignore
                    ),
                    None,
                )
            else:
                return arg, None

        while True:
            for transform in [_handle_generics] + _argument_transforms:  # type: ignore
                # Apply transform.
                arg, new_role = transform(arg)

                # Update field role.
                if new_role is not None:
                    assert (
                        role == _construction.FieldRoleEnum.VANILLA_FIELD
                    ), "Something went wrong -- only one field role can be specified per argument!"
                    role = new_role

            # Stability check.
            if arg == prev_arg:
                break
            prev_arg = arg
        return arg, role


# Argument transformations.
# Each transform returns an argument definition and (optionall) a special role for
# reconstruction -- note that a field can only ever have one role.

_ArgumentTransformOutput = Tuple[ArgumentDefinition, Optional[_construction.FieldRole]]


def _unwrap_final(arg: ArgumentDefinition) -> _ArgumentTransformOutput:
    """Treat Final[T] as just T."""
    if get_origin(arg.type) is Final:
        (typ,) = get_args(arg.type)
        return (
            dataclasses.replace(
                arg,
                type=typ,
            ),
            None,
        )
    else:
        return arg, None


def _unwrap_annotated(arg: ArgumentDefinition) -> _ArgumentTransformOutput:
    """Treat Annotated[T, annotation] as just T."""
    if hasattr(arg.type, "__class__") and arg.type.__class__ == _AnnotatedAlias:
        typ = get_origin(arg.type)
        return (
            dataclasses.replace(
                arg,
                type=typ,
            ),
            None,
        )
    else:
        return arg, None


def _handle_optionals(arg: ArgumentDefinition) -> _ArgumentTransformOutput:
    """Transform for handling Optional[T] types. Sets default to None and marks arg as
    not required."""
    if get_origin(arg.type) is Union:
        options = set(get_args(arg.type))
        assert (
            len(options) == 2 and type(None) in options
        ), "Union must be either over dataclasses (for subparsers) or Optional"
        (typ,) = options - {type(None)}
        required = False
        return (
            dataclasses.replace(
                arg,
                type=typ,
                required=required,
            ),
            None,
        )
    else:
        return arg, None


def _populate_defaults(arg: ArgumentDefinition) -> _ArgumentTransformOutput:
    """Populate default values."""
    if arg.default is not None:
        # Skip if another handler has already populated the default.
        return arg, None

    default = None
    required = True
    if arg.field.default is not dataclasses.MISSING:
        default = arg.field.default
        required = False
    elif arg.field.default_factory is not dataclasses.MISSING:  # type: ignore
        default = arg.field.default_factory()  # type: ignore
        required = False

    if arg.required is not None:
        required = arg.required

    return dataclasses.replace(arg, default=default, required=required), None


def _bool_flags(arg: ArgumentDefinition) -> _ArgumentTransformOutput:
    """For booleans, we use a `store_true` action."""
    if arg.type != bool:
        return arg, None

    # Populate helptext for boolean flags => don't show default value, which can be
    # confusing.
    docstring_help = _docstrings.get_field_docstring(arg.parent_class, arg.field.name)
    if docstring_help is not None:
        # Note that the percent symbol needs some extra handling in argparse.
        # https://stackoverflow.com/questions/21168120/python-argparse-errors-with-in-help-string
        docstring_help = docstring_help.replace("%", "%%")
        arg = dataclasses.replace(
            arg,
            help=docstring_help,
        )
    else:
        arg = dataclasses.replace(
            arg,
            help="",
        )

    if arg.default is None:
        return (
            dataclasses.replace(
                arg,
                metavar="{True,False}",
            ),
            None,
        )
    elif arg.default is False:
        return (
            dataclasses.replace(
                arg,
                action="store_true",
                type=None,
            ),
            None,
        )
    elif arg.default is True:
        return (
            dataclasses.replace(
                arg,
                dest=arg.name,
                name="no_" + arg.name,
                action="store_false",
                type=None,
            ),
            None,
        )
    else:
        assert False, "Invalid default"


def _nargs_from_sequences_lists_and_sets(
    arg: ArgumentDefinition,
) -> _ArgumentTransformOutput:
    """Transform for handling Sequence[T] and list types."""
    if get_origin(arg.type) in (
        collections.abc.Sequence,  # different from typing.Sequence!
        list,  # different from typing.List!
        set,  # different from typing.Set!
    ):
        (typ,) = get_args(arg.type)
        role = get_origin(arg.type)
        if role is collections.abc.Sequence:
            role = list

        return (
            dataclasses.replace(
                arg,
                type=typ,
                # `*` is >=0 values, `+` is >=1 values
                # We're going to require at least 1 value; if a user wants to accept no
                # input, they can use Optional[Tuple[...]]
                nargs="+",
            ),
            role,
        )
    else:
        return arg, None


def _nargs_from_tuples(arg: ArgumentDefinition) -> _ArgumentTransformOutput:
    """Transform for handling Tuple[T, T, ...] types."""

    if arg.nargs is None and get_origin(arg.type) is tuple:
        types = get_args(arg.type)
        typeset = set(types)
        typeset_no_ellipsis = typeset - {Ellipsis}

        if typeset_no_ellipsis != typeset:
            # Ellipsis: variable argument counts
            assert (
                len(typeset_no_ellipsis) == 1
            ), "If ellipsis is used, tuples must contain only one type."
            (typ,) = typeset_no_ellipsis

            return (
                dataclasses.replace(
                    arg,
                    # `*` is >=0 values, `+` is >=1 values.
                    # We're going to require at least 1 value; if a user wants to accept no
                    # input, they can use Optional[Tuple[...]].
                    nargs="+",
                    type=typ,
                ),
                tuple,
            )
        else:
            # Tuples with more than one type
            assert arg.metavar is None

            return (
                dataclasses.replace(
                    arg,
                    nargs=len(types),
                    type=str,  # Types will be converted in the dataclass reconstruction step.
                    metavar=tuple(
                        t.__name__.upper() if hasattr(t, "__name__") else "X"
                        for t in types
                    ),
                ),
                # Field role: convert lists of strings to tuples of the correct types.
                lambda str_list: tuple(
                    _instance_from_string(typ, x) for typ, x in zip(types, str_list)
                ),
            )

    else:
        return arg, None


def _choices_from_literals(arg: ArgumentDefinition) -> _ArgumentTransformOutput:
    """For literal types, set choices."""
    if get_origin(arg.type) is Literal:
        choices = set(get_args(arg.type))
        assert (
            len(set(map(type, choices))) == 1
        ), "All choices in literal must have the same type!"
        return (
            dataclasses.replace(
                arg,
                type=type(next(iter(choices))),
                choices=choices,
            ),
            None,
        )
    else:
        return arg, None


def _enums_as_strings(arg: ArgumentDefinition) -> _ArgumentTransformOutput:
    """For enums, use string representations."""
    if isinstance(arg.type, type) and issubclass(arg.type, enum.Enum):
        if arg.choices is None:
            choices = set(x.name for x in arg.type)
        else:
            choices = set(x.name for x in arg.choices)

        return (
            dataclasses.replace(
                arg,
                choices=choices,
                type=str,
                default=None if arg.default is None else arg.default.name,
            ),
            lambda enum_name: arg.type[enum_name],  # type: ignore
        )
    else:
        return arg, None


def _generate_helptext(arg: ArgumentDefinition) -> _ArgumentTransformOutput:
    """Generate helptext from docstring and argument name."""
    if arg.help is None:
        help_parts = []
        docstring_help = _docstrings.get_field_docstring(
            arg.parent_class, arg.field.name
        )
        if docstring_help is not None:
            # Note that the percent symbol needs some extra handling in argparse.
            # https://stackoverflow.com/questions/21168120/python-argparse-errors-with-in-help-string
            docstring_help = docstring_help.replace("%", "%%")
            help_parts.append(docstring_help)

        if arg.default is not None and hasattr(arg.default, "name"):
            # Special case for enums.
            help_parts.append(f"(default: {arg.default.name})")
        elif not arg.required:
            # General case.
            help_parts.append("(default: %(default)s)")

        return dataclasses.replace(arg, help=" ".join(help_parts)), None
    else:
        return arg, None


def _use_type_as_metavar(arg: ArgumentDefinition) -> _ArgumentTransformOutput:
    """Communicate the argument type using the metavar."""
    if hasattr(arg.type, "__name__") and arg.choices is None and arg.metavar is None:
        return (
            dataclasses.replace(arg, metavar=arg.type.__name__.upper()),  # type: ignore
            None,
        )
    else:
        return arg, None


_argument_transforms: List[Callable[[ArgumentDefinition], _ArgumentTransformOutput]] = [
    _unwrap_final,
    _unwrap_annotated,
    _handle_optionals,
    _populate_defaults,
    _bool_flags,
    _nargs_from_sequences_lists_and_sets,
    _nargs_from_tuples,
    _choices_from_literals,
    _enums_as_strings,
    _generate_helptext,
    _use_type_as_metavar,
]
