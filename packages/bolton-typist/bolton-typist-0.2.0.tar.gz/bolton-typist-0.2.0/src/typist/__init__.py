"""Typing utilities we wish were in the standard library."""

import logging as _logging

from ._core import (
    Comparable,
    DateLike,
    PathLike,
    ToDictable,
    assert_never,
    is_jsonable,
    literal_to_list,
)


__all__ = [
    "Comparable",
    "DateLike",
    "PathLike",
    "ToDictable",
    "assert_never",
    "is_jsonable",
    "literal_to_list",
]

__author__ = "Bryan M Bugyi"
__email__ = "bryanbugyi34@gmail.com"
__version__ = "0.2.0"

_logging.getLogger(__name__).addHandler(_logging.NullHandler())
