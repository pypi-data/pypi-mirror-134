"""
Constant values used in the didyou package.
"""
from enum import Enum
from typing import Callable

from didyou.utils import similarity


class Constants(Enum):
    """
    Constant values used in the didyou package.
    """
    DEFAULT_SIMILARITY_FUNCTION: Callable[[str, str], float] = similarity
    DEFAULT_SIMILARITY_THRESHOLD: float = 0.75
