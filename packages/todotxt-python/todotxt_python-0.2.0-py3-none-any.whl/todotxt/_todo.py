"""Contains the Todo class definition."""

from __future__ import annotations

from dataclasses import dataclass
import datetime as dt
import re
from typing import Dict, Final, List, Optional, Tuple, cast

from eris import ErisError, Err, Ok, Result

from ._dates import RE_DATE, to_date
from .types import Priority


DEFAULT_PRIORITY: Final[Priority] = "N"
PROJECT_PREFIX: Final = "+"
CONTEXT_PREFIX: Final = "@"

RE_TODO: Final = r"""
(?P<x>x[ ]+)?                        # optional 'x'
\((?P<priority>[A-Z])\)[ ]+          # priority
(?:
    (?:(?P<done_date>{0})[ ]+)?      # optional date of completion
    (?:(?P<create_date>{0})[ ]+)     # optional date of creation
)?
(?P<desc>.*)                         # description
""".format(
    RE_DATE
)


@dataclass(frozen=True)
class Todo:
    """Represents a single task in a todo list."""

    desc: str

    contexts: Tuple[str, ...] = ()
    create_date: Optional[dt.date] = None
    done_date: Optional[dt.date] = None
    marked_done: bool = False
    metadata: Optional[Dict[str, str]] = None
    priority: Priority = DEFAULT_PRIORITY
    projects: Tuple[str, ...] = ()

    @classmethod
    def from_string(cls, string: str) -> Result[Todo, ErisError]:
        """Contructs a Todo object from a string (usually a line in a file)."""
        re_todo_match = re.match(RE_TODO, string, re.VERBOSE)
        if re_todo_match is None:
            return Err(
                f"The provided string ({string!r}) does not appear to properly"
                " adhere to the todo.txt format. See"
                " https://github.com/todotxt/todo.txt for the specification."
            )

        marked_done: bool = False
        if re_todo_match.group("x"):
            marked_done = True

        priority: Priority = DEFAULT_PRIORITY
        if grp := re_todo_match.group("priority"):
            priority = cast(Priority, grp)

        create_date: Optional[dt.date] = None
        if grp := re_todo_match.group("create_date"):
            create_date = to_date(grp)

        done_date: Optional[dt.date] = None
        if grp := re_todo_match.group("done_date"):
            done_date = to_date(grp)

        desc = re_todo_match.group("desc")
        all_words = desc.split(" ")

        project_list: List[str] = []
        context_list: List[str] = []
        for some_list, prefix in [
            (project_list, PROJECT_PREFIX),
            (context_list, CONTEXT_PREFIX),
        ]:
            for word in all_words:
                if word.startswith(prefix):
                    some_list.append(word[len(prefix) :])

        projects = tuple(project_list)
        contexts = tuple(context_list)

        metadata: Optional[Dict[str, str]] = None
        mdata: Dict[str, str] = {}
        for word in all_words:
            kv = word.split(":", maxsplit=1)
            if len(kv) == 2:
                key, value = kv
                mdata[key] = value

        if mdata:
            metadata = mdata

        todo = Todo(
            contexts=contexts,
            create_date=create_date,
            desc=desc,
            done_date=done_date,
            marked_done=marked_done,
            metadata=metadata,
            priority=priority,
            projects=projects,
        )
        return Ok(todo)
