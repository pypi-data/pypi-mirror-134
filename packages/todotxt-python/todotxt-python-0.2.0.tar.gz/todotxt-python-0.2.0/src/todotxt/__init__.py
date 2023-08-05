"""A Python library for working with the todo.txt format."""

import logging as _logging

from . import types
from ._helpers import read_todos_from_file
from ._todo import DEFAULT_PRIORITY, Todo


__all__ = ["DEFAULT_PRIORITY", "Todo", "read_todos_from_file", "types"]

__author__ = "Bryan M Bugyi"
__email__ = "bryanbugyi34@gmail.com"
__version__ = "0.2.0"

_logging.getLogger(__name__).addHandler(_logging.NullHandler())
