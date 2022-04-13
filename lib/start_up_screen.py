#!/usr/bin/env python3

from typing import List, Tuple
from lib.terminal_display_object import TerminalDisplayObject
from lib.terminal_display import TerminalDisplay


class StartUpScreen(TerminalDisplayObject):
    """A screen to be displayed to the user upon starting up the game."""
    def __init__(self, terminal_display: TerminalDisplay):
        # screens like this and the pause menu should be on to of everything
        depth = 0

        # this should come before the rest of the setup
        # so that class attributes are correctly set
        super().__init__(name="start_up",
                         depth=depth,
                         terminal_display=terminal_display)

        self.message = "Let's play Snake!"
        self.message_length = len("Let's play Snake!")

        # call only after setting message and message length
        self.chars = self._get_start_up_chars()

    def _get_start_up_chars(self) -> List[Tuple[int, int, str]]:
        """The start up displays a message text should be centered.

        fill in blank space above and below the text
        """
        # to shorten some of the logic to follow, use an alias
        td = self.terminal_display

        # find middle row
        middle_row = td.rows // 2

        # compute off-set based on length
        offset = td.columns // 2 - self.message_length // 2

        start_up_chars = [(middle_row, j, char)
                          for j, char in zip(
                              list(range(offset, self.message_length+offset)),
                              self.message
                         )]
        return start_up_chars
