"""The potoroo package's catch-all module.

You should only add code to this module when you are unable to find ANY other
module to add it to.
"""

from __future__ import annotations

import abc
from typing import Generic, TypeVar

from eris import ErisResult


K = TypeVar("K")
V = TypeVar("V")


class Repository(Generic[K, V], abc.ABC):
    """A persistance pattern meant to abstract away data acess details.

    See https://deviq.com/design-patterns/repository-pattern/ for more
    information.
    """

    @abc.abstractmethod
    def add(self, item: V) -> ErisResult[K]:
        """Add a new `item` to the repo and associsate it with `key`."""

    @abc.abstractmethod
    def get(self, key: K) -> ErisResult[V | None]:
        """Retrieve an item from the repo by key."""

    @abc.abstractmethod
    def remove(self, key: K) -> ErisResult[V | None]:
        """Remove an item from the repo by key."""

    @abc.abstractmethod
    def update(self, key: K, item: V) -> ErisResult[V]:
        """Update an item by key."""
