"""
State Index type.

Generic type for index States.

Currently allowed types:
    - int
    - str
    - Tuple
"""

from typing import Tuple

# TODO Test the types allowed.
type StateIndex = int | str | Tuple[int, ...]
