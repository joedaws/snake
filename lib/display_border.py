#!/usr/bin/env python3

from typing import List, Tuple
from lib.terminal_display_object import TerminalDisplayObject
from lib.terminal_display import TerminalDisplay


WALL_CHAR = '│'
UPPER_RIGHT_CHAR = '┐'
LOWER_RIGHT_CHAR = '┘'
LOWER_LEFT_CHAR = '└'
UPPER_LEFT_CHAR = '┌'
BOX_HORIZONTAL_CHAR = '─'


class Border(TerminalDisplayObject):
    """A board to be draw around the playing field"""
    def __init__(self, terminal_display: TerminalDisplay):
        # Border should appear ontop of pretty much all other objects
        depth = 1

        # this should come before the rest of the setup
        # so that class attributes are correctly set
        super().__init__(name="border",
                         depth=depth,
                         terminal_display=terminal_display)


        # (0, 0) assumes the top boarder is the very top of the display
        self.top_left_coord = (0, 0)
        # this assumes the border goes all the way to the bottom of the
        # display
        self.bottom_right_coord = (self.terminal_display.rows-1,
                                   self.terminal_display.columns-1)

        # call only after setting up top_left_coord and bottom_right_coord
        self.chars = self._get_border_chars()

    def _get_border_chars(self) -> List[Tuple[int, int, str]]:
        """The border is drawn with respect to the size of the TerminalDisplay.

        Let td be short hand for the terminal display object
        Let (i,j) be the coordinates of the top left corder of the grid, then
        the top row has coordinates
        (i,  j)  (i  , j+1) ... (i  , j+(td.columns - 1))

        The walls on row k have coordinates for
        i<k<bottom_right_coord[0]
        (i+k, j) and (i+k, j+td.columns)

        The bottom row has coordinates
        (i+(td.rows-1),j)  ... (i+(td.rows-1), j+(td.columns-1))
        ...
        """
        # to shorten some of the logic to follow, use an alias
        td = self.terminal_display

        i, j = self.top_left_coord
        top_border = [(i, j, UPPER_LEFT_CHAR)]
        top_border += [(i, j+k, BOX_HORIZONTAL_CHAR)
                       for k in range(1, td.columns-1)]
        top_border += [(i, j+td.columns-1, UPPER_RIGHT_CHAR)]

        walls = [(i+k, l, WALL_CHAR) for l in [j, j+self.bottom_right_coord[1]]
                 for k in range(i+1, self.bottom_right_coord[0])]

        bottom_border = [(i+(td.rows-1), j, LOWER_LEFT_CHAR)]
        bottom_border += [(i+(td.rows-1), j+k, BOX_HORIZONTAL_CHAR)
                          for k in range(1, td.columns-1)]
        bottom_border += [(i+(td.rows-1), j+td.columns-1, LOWER_RIGHT_CHAR)]

        return top_border + walls + bottom_border
