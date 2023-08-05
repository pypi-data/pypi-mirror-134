"""The catch-all module for the tests.data package."""

from pathlib import Path
from typing import List


def get_all_todo_files() -> List[Path]:
    """Returns the full path of every todo.txt file in the todos directory."""
    todo_dir_path = Path(__file__).absolute().parent / "todos"

    result = []

    for txt in todo_dir_path.glob("*.txt"):
        result.append(txt)

    return result
