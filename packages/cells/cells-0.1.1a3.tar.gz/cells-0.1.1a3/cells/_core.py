import importlib
import re
from functools import lru_cache
from typing import Dict, List

from cells._terminal_support import _detect_unicode_version
from ._lru_cache import LRUCache

_is_single_cell_widths = re.compile("^[\u0020-\u006f\u00a0\u02ff\u0370-\u0482]*$").match

SUPPORTED_UNICODE_VERSIONS: List[str] = [
    "auto",
    "4.1.0",
    "5.0.0",
    "5.1.0",
    "5.2.0",
    "6.0.0",
    "6.1.0",
    "6.2.0",
    "6.3.0",
    "7.0.0",
    "8.0.0",
    "9.0.0",
    "10.0.0",
    "11.0.0",
    "12.0.0",
    "12.1.0",
    "13.0.0",
]


class UnsupportedUnicodeVersion(Exception):
    pass


class BaseCells:
    def measure(self, text: str) -> int:  # pragma: no cover
        raise NotImplementedError


class Cells(BaseCells):
    def __init__(self, unicode_version: str = "auto", cache_size: int = 4096) -> None:
        """
        Args:
            unicode_version (str): String version of the Unicode database to use.
                Defaults to "auto", which will make a best-effort attempt to detect the
                Unicode version supported by the current terminal program. If the version
                cannot be detected, Cells will fallback to Unicode 9.0.
            cache_size (int): Number of entries to store in the measurement cache
        """
        if unicode_version == "auto":
            unicode_version = _detect_unicode_version()

        if unicode_version not in SUPPORTED_UNICODE_VERSIONS:
            raise UnsupportedUnicodeVersion(
                f"Unicode version {unicode_version} not supported. "
                f"Supported Unicode versions: {SUPPORTED_UNICODE_VERSIONS}"
            )
        self.unicode_version: str = unicode_version

        self._cache: Dict[str, int] = LRUCache(cache_size=cache_size)

        database_module = f".databases.unicode_{unicode_version.replace('.', '')}"
        self.unicode_database = importlib.import_module(
            name=database_module, package="cells"
        )

    def measure(self, text: str) -> int:
        """Get the cell width of a string of text

        Args:
            text (str): A string of text to be measured.

        Returns:
            int: The total number of cells (width) occupied by that text.
        """
        if _is_single_cell_widths(text):
            return len(text)
        cached_result = self._cache.get(text)
        if cached_result is not None:
            return cached_result
        measure_char = self._measure_character
        total_size = sum(measure_char(char) for char in text)
        if len(text) <= 64:
            self._cache[text] = total_size
        return total_size

    @lru_cache(maxsize=4096)
    def _measure_character(self, character: str) -> int:
        """Get the cell width of a single character.

        Args:
            character (str): A single character.

        Returns:
            int: Number of cells (0, 1 or 2) occupied by the character.
        """
        if _is_single_cell_widths(character):
            return 1
        return self._measure_codepoint(ord(character))

    @lru_cache(maxsize=4096)
    def _measure_codepoint(self, codepoint: int) -> int:
        """Get the cell width of a single Unicode codepoint

        Args:
            codepoint (int): The Unicode codepoint specified as an int

        Returns:
            int: Number of cells (0, 1 or 2) occupied by the codepoint.
        """
        _table = getattr(self.unicode_database, "CELL_WIDTHS")
        lower_bound = 0
        upper_bound = len(_table) - 1
        index = (lower_bound + upper_bound) // 2
        while True:
            start, end, width = _table[index]
            if codepoint < start:
                upper_bound = index - 1
            elif codepoint > end:
                lower_bound = index + 1
            else:
                return 0 if width == -1 else width
            if upper_bound < lower_bound:
                break
            index = (lower_bound + upper_bound) // 2
        return 1

    def normalize(self, text: str) -> str:
        """
        Args:
            text (str): Text sequence to normalize.

        Returns:
            str: Normalized version of the text sequence.
        """
        raise NotImplementedError
