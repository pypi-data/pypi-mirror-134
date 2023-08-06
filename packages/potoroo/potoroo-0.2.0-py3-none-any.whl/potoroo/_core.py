"""The potoroo package's catch-all module.

You should only add code to this module when you are unable to find ANY other
module to add it to.
"""

from __future__ import annotations

import abc
from typing import Generic, TypeVar

from eris import ErisResult


T = TypeVar("T")
K = TypeVar("K")


class Repository(Generic[T, K], abc.ABC):
    """A persistance pattern meant to abstract away data acess details.

    See https://deviq.com/design-patterns/repository-pattern/ for more
    information.
    """

    @abc.abstractmethod
    def add(self, item: T) -> ErisResult[K]:
        """Add a new `item` to the repo and associsate it with `key`."""

    @abc.abstractmethod
    def get(self, key: K) -> ErisResult[T | None]:
        """Retrieve an item from the repo by key."""

    @abc.abstractmethod
    def remove(self, key: K) -> ErisResult[T | None]:
        """Remove an item from the repo by key."""

    @abc.abstractmethod
    def update(self, key: K, item: T) -> ErisResult[T]:
        """Update an item by key."""
