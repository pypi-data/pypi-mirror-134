"""
Main stuff for the mean command.
"""

from typing import Callable, List

from didyou.constants import Constants


#pylint: disable=too-few-public-methods
class Mean:
    """
    didyou.mean(this)
    """

    def __init__(
        self,
        *,
        allowed_words: List[str],
        similarity_function: Callable[[str, str], float] = None,
        similarity_threshold: float = None,
    ):
        """
        Initialize the Mean class.
        """
        self._allowed_words = allowed_words
        self._similarity_function = similarity_function or Constants.DEFAULT_SIMILARITY_FUNCTION
        self._similarity_threshold = similarity_threshold or \
            Constants.DEFAULT_SIMILARITY_THRESHOLD.value

    def __call__(self, this: str) -> str:
        """
        Return the closest word to the given word.
        """
        best_similarity = 0
        best_word = ""
        for word in self._allowed_words:
            similarity = self._similarity_function(this, word)
            if similarity > best_similarity:
                best_similarity = similarity
                best_word = word
        if best_similarity >= self._similarity_threshold:
            return best_word
        return None


def mean(
    this,
    *,
    allowed_words: List[str],
    similarity_function: Callable[[str, str], float] = None,
    similarity_threshold: float = None,
) -> str:
    """
    Return the closest word to the given word.
    """
    return Mean(
        allowed_words=allowed_words,
        similarity_function=similarity_function,
        similarity_threshold=similarity_threshold,
    )(this)
