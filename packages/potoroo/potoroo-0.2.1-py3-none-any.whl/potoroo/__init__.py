"""Python implementations of the Repository and UnitOfWork abstractions."""

import logging as _logging

from ._core import Repository


__all__ = ["Repository"]

__author__ = "Bryan M Bugyi"
__email__ = "bryanbugyi34@gmail.com"
__version__ = "0.2.1"

_logging.getLogger(__name__).addHandler(_logging.NullHandler())
