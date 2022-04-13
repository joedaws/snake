#!/usr/bin/env python3

from typing import List
from enum import Enum


SPACE_BLANK_CHAR = ' '
GRAY_SQUARE_BLANK_CHAR = '░'
WALL_CHAR = '│'
UPPER_RIGHT_CHAR = '┐'
LOWER_RIGHT_CHAR = '┘'
LOWER_LEFT_CHAR = '└'
UPPER_LEFT_CHAR = '┌'
BOX_HORIZONTAL_CHAR = '─'


class BlankCharType(Enum):
    """The allowed types of blank characters"""
    SPACE = "space"
    GRAY_SQUARE = "gray_square"


blank_char_type_to_char = {
    BlankCharType.SPACE: SPACE_BLANK_CHAR,
    BlankCharType.GRAY_SQUARE: GRAY_SQUARE_BLANK_CHAR
}


class TerminalDisplay:
    """
    This class holds all of the characters which will be displayed.

    It also has an name_to_object hash which is used to register objects
    which will be displayed on the terminal display.

    when adding objects, the chars attribute is always updated
    when removing objects, the chars attribute is always updated.
    """
    def __init__(self,
                 rows: int = 12,
                 columns: int = 42,
                 blank_char: str = "space"):
        self.rows = rows
        self.columns = columns
        self.blank_char_type = BlankCharType(blank_char)
        self.chars = self._blank_terminal_display()
        self.name_to_object = {}

    def add_object(self, obj):
        """This function adds an object to both the name_to_object map
        as well as updates the chars attribute.

        Also checks for collision and prioritizes drawing by depth
        """
        for char_tup in obj.chars:
            i, j, char = char_tup
            self.chars[i][j] = char

        self.name_to_object[obj.name] = obj

    def remove_object(self, name):
        """This function removes an object to both the name_to_object map
        as well as updates the chars attribute.
        """
        out_obj = self.name_to_object.pop(name)

        for char_tup in out_obj.chars:
            i, j, _ = char_tup
            self.chars[i][j] = blank_char_type_to_char[self.blank_char_type]

        return out_obj

    def _blank_terminal_display(self):
        """
        Blanks out the terminal display
        - n is number of rows
        - m is number of columns
        - blank_char_type is the type of character to use as blank space in the
        display
        """
        blank_char = blank_char_type_to_char[self.blank_char_type]
        return [[blank_char]*self.columns for _ in range(self.rows)]

    def __str__(self):
        return draw(self.chars)


def draw(grid: List[List[str]]) -> str:
    """Takes a list of rows (which are lists of chars)
    and converts them to a string."""
    out_str = ""
    for row in grid:
        for char in row:
            out_str += char
        # new line at the end of each row
        out_str += '\n'
    return out_str
