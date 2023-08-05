"""Test the helper utilities provided by the todotxt library."""

from __future__ import annotations

from pathlib import Path

from pytest import mark
from syrupy.assertion import SnapshotAssertion as Snapshot

import todotxt

from .data import get_all_todo_files


params = mark.parametrize


@params("todo_file", get_all_todo_files())
def test_read_todos_from_file(snapshot: Snapshot, todo_file: Path) -> None:
    """Test the read_todos_from_file() function."""
    todos = todotxt.read_todos_from_file(todo_file)
    assert [todo.__dict__ for todo in todos] == snapshot
