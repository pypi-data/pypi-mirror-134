"""
General utilities for the didyou package.
"""

from difflib import SequenceMatcher


def similarity(word1: str, word2: str) -> float:
    """
    Compute the similarity between two words.
    """
    return SequenceMatcher(None, word1, word2).ratio()
