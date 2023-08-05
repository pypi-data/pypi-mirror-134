"""Helper utilities provided by the todotxt library."""

from pathlib import Path
from typing import List

from eris import Err
from typist import PathLike

from ._todo import Todo


def read_todos_from_file(path_like: PathLike) -> List[Todo]:
    """Reads all todo lines from a given file.

    Pre-conditions:
        * `path_like` exists and is a file.
    """
    path = Path(path_like)

    assert (
        path.is_file()
    ), f"The provided path does not exist or is not a file: {path}"

    todos_in_file = []
    for line in path.read_text().split("\n"):
        line = line.strip()
        todo_result = Todo.from_string(line)
        if isinstance(todo_result, Err):
            continue

        todo = todo_result.ok()
        todos_in_file.append(todo)

    return todos_in_file
