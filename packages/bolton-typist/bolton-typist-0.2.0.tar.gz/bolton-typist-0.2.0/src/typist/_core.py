"""The typist package's catch-all module.

You should only add code to this module when you are unable to find ANY other
module to add it to.
"""

from __future__ import annotations

import datetime as dt
from enum import Enum
import json
from pathlib import Path
from typing import Any, List, NoReturn, Protocol, TypeVar, Union, get_args


Comp_T = TypeVar("Comp_T", bound="Comparable")

DateLike = Union[str, dt.date, dt.datetime]
PathLike = Union[str, Path]


class ToDictable(Protocol):
    """Any object with a to_dict() method."""

    def to_dict(self) -> dict[str, Any]:
        """Converts this object to a dictionary."""


class Comparable(Protocol):
    """A type that can be compared and sorted."""

    def __eq__(self, other: Any) -> bool:  # noqa: D105
        pass

    def __lt__(self: Comp_T, other: Comp_T) -> bool:  # noqa: D105
        pass

    def __gt__(self: Comp_T, other: Comp_T) -> bool:  # noqa: D105
        pass

    def __le__(self: Comp_T, other: Comp_T) -> bool:  # noqa: D105
        pass

    def __ge__(self: Comp_T, other: Comp_T) -> bool:  # noqa: D105
        pass


def assert_never(value: NoReturn) -> NoReturn:
    """
    Raises an AssertionError. This function can be used to achieve
    exhaustiveness checking with mypy.

    REFERENCE: https://hakibenita.com/python-mypy-exhaustive-checking
    """
    raise AssertionError(f"Unhandled value: {value} ({type(value).__name__})")


def literal_to_list(
    literal: Any,
) -> List[Union[None, bool, bytes, int, str, Enum]]:
    """
    Convert a typing.Literal into a list.

    Examples:
        >>> from typing import Literal
        >>> literal_to_list(Literal['a', 'b', 'c'])
        ['a', 'b', 'c']

        >>> literal_to_list(Literal['a', 'b', Literal['c', 'd', Literal['e']]])
        ['a', 'b', 'c', 'd', 'e']

        >>> literal_to_list(Literal['a', 'b', Literal[1, 2, Literal[None]]])
        ['a', 'b', 1, 2, None]
    """
    result = []

    for arg in get_args(literal):
        if arg is None or isinstance(arg, (bool, bytes, int, str, Enum)):
            result.append(arg)
        else:
            result.extend(literal_to_list(arg))

    return result


def is_jsonable(obj: Any) -> bool:
    """Check if an object can be serialized to JSON.

    Args:
        obj: The object we want to serialize to JSON.

    Returns:
        True iff ``obj`` is JSON serializable.

    Examples:
        >>> is_jsonable("hi")
        True

        >>> is_jsonable(123)
        True

        >>> is_jsonable({"sets", "cannot", "be", "serialized", "to", "json"})
        False
    """
    try:
        json.dumps(obj)
        return True
    except (TypeError, OverflowError):
        return False
