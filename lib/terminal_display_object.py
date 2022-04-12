#!/usr/bin/env python3

from typing import List, Tuple
from abc import ABC
from lib.terminal_display import TerminalDisplay


DEFAULT_CHARS = [(0, 0, "")]


class TerminalDisplayObject(ABC):
    """
    An object which is displayed with in the terminal display.

    Has a name and a

    """
    def __init__(self,
                 name: str,
                 depth: int,
                 terminal_display: TerminalDisplay):

        self.name = name
        self.depth = depth
        self.terminal_display = terminal_display
        self._chars = DEFAULT_CHARS

    @property
    def chars(self) -> List[Tuple[int, int, str]]:
        """The list of tuples which describes the chars in this object."""
        return self._chars

    @chars.setter
    def chars(self, new_chars: List[Tuple[int, int, str]]) -> None:
        self._chars = new_chars

    def __str__(self):
        out_str = "Terminal Display Object: \n"
        out_str += f"  name: {self.name}\n"
        for i, char_tup in enumerate(self.chars):
            out_str += f"  char {i}: {char_tup[0]} {char_tup[1]} {char_tup[2]}"
        return out_str
