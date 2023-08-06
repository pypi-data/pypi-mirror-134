"""Tests for the potoroo package."""

from __future__ import annotations

from eris import ErisResult, Ok

from potoroo import Repository


class FakeDB(Repository[int, str]):
    """Fake database."""

    def __init__(self) -> None:
        self._keys = list(range(100))
        self._db: dict[int, str] = {}

    def add(self, item: str) -> ErisResult[int]:
        """Fake add."""
        key = self._keys.pop(0)
        self._db[key] = item
        return Ok(key)

    def get(self, key: int) -> ErisResult[str | None]:
        """Fake get."""
        return Ok(self._db[key])

    def remove(self, key: int) -> ErisResult[str | None]:
        """Fake remove."""
        return Ok(self._db.pop(key))

    def update(self, key: int, item: str) -> ErisResult[str]:
        """Fake update."""
        self._db[key] = item
        return Ok(item)


def test_repo() -> None:
    """Test the Repository type."""
    db = FakeDB()
    foo_idx = db.add("foo").unwrap()
    assert db.get(foo_idx).unwrap() == "foo"
    assert db.update(foo_idx, "bar").unwrap() == "bar"
    assert db.remove(foo_idx).unwrap() == "bar"
