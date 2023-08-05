"""Tests for the todotxt package."""

from __future__ import annotations

from pytest import mark

from todotxt import Todo
from todotxt._dates import to_date


params = mark.parametrize


@params(
    "line,expected",
    [
        ("(N) basic todo", Todo(desc="basic todo")),
        (
            "(N) 2022-01-10 todo with create date",
            Todo(
                desc="todo with create date",
                create_date=to_date("2022-01-10"),
            ),
        ),
        (
            "(N) 2022-03-04 2022-01-10 todo with done date",
            Todo(
                desc="todo with done date",
                create_date=to_date("2022-01-10"),
                done_date=to_date("2022-03-04"),
            ),
        ),
        (
            "x (N) 2022-01-10 done todo",
            Todo(
                desc="done todo",
                create_date=to_date("2022-01-10"),
                marked_done=True,
            ),
        ),
        (
            "x (A) todo with priority",
            Todo(
                desc="todo with priority",
                marked_done=True,
                priority="A",
            ),
        ),
        (
            "(N) todo for +some +project",
            Todo(
                desc="todo for +some +project",
                projects=("some", "project"),
            ),
        ),
        (
            "(N) todo for +some +project and a @context",
            Todo(
                desc="todo for +some +project and a @context",
                projects=("some", "project"),
                contexts=("context",),
            ),
        ),
        (
            "(N) todo with +some meta:data and a @context due:2022-12-31",
            Todo(
                desc="todo with +some meta:data and a @context due:2022-12-31",
                projects=("some",),
                contexts=("context",),
                metadata={"meta": "data", "due": "2022-12-31"},
            ),
        ),
    ],
)
def test_todo(line: str, expected: Todo) -> None:
    """Test the Todo type."""
    actual = Todo.from_string(line)
    assert actual.unwrap() == expected
