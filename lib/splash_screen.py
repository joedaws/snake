#!/usr/bin/env python3
"""
Displays flashing snake word for now
"""

from enum import Enum, auto
from typing import List, Tuple
from lib.terminal_display_object import TerminalDisplayObject
from lib.terminal_display import TerminalDisplay


SNAKE_WORD = [
    " ____              _        ",
    "/ ___| _ __   __ _| | _____ ",
    "\\___ \\| '_ \\ / _` | |/ / _ \\",
    " ___) | | | | (_| |   <  __/",
    "|____/|_| |_|\\__,_|_|\\_\\___|",
]

SNAKE_WORD_2 = \
"                   _         \n" +\
"       _ __   __ _| | _____  \n" +\
"      | '_ \ / _` | |/ / _ \ \n" +\
"      | | | | (_| |   <  __/ \n" +\
"      |_| |_|\__,_|_|\_\___| \n"

SNAKE_WORD_3 = \
" ____              _         \n" +\
"/ ___|        __ _| | _____  \n" +\
"\___ \       / _` | |/ / _ \ \n" +\
" ___) |     | (_| |   <  __/ \n" +\
"|____/       \__,_|_|\_\___| \n"

SNAKE_WORD_4 = \
" ____              _         \n" +\
"/ ___| _ __       | | _____  \n" +\
"\___ \| '_ \      | |/ / _ \ \n" +\
" ___) | | | |     |   <  __/ \n" +\
"|____/|_| |_|     |_|\_\___| \n"

SNAKE_WORD_5 = \
" ____                        \n" +\
"/ ___| _ __   __ _      ___  \n" +\
"\___ \| '_ \ / _` |    / _ \ \n" +\
" ___) | | | | (_| |    | __/ \n" +\
"|____/|_| |_|\__,_|    \___| \n"

SNAKE_WORD_6 = \
" ____              _         \n" +\
"/ ___| _ __   __ _| | __     \n" +\
"\___ \| '_ \ / _` | |/ /     \n" +\
" ___) | | | | (_| |   <      \n" +\
"|____/|_| |_|\__,_|_|\_\     \n"


class SplashMenuItems(Enum):
    """Defines the options for modes of play."""
    CLASSIC = auto()
    STORY = auto()
    VERSUS = auto()


class SplashScreen(TerminalDisplayObject):
    """A screen to be displayed with the options for playing."""
    def __init__(self, terminal_display: TerminalDisplay):
        # screens like this and the pause menu should be on to of everything
        depth = 0

        # this should come before the rest of the setup
        # so that class attributes are correctly set
        super().__init__(name="splash",
                         depth=depth,
                         terminal_display=terminal_display)

        # determines where the word starts
        self.top_left_point = (1, 1)

        # call only after setting message and message length
        self.chars = self._get_splash_chars()

    def _get_splash_chars(self) -> List[Tuple[int, int, str]]:
        """The start up displays a message text should be centered.

        fill in blank space above and below the text
        """
        # to shorten some of the logic to follow, use an alias
        td = self.terminal_display
        tlx, tly = self.top_left_point

        snake_word_chars = []
        i = tlx
        for row in SNAKE_WORD:
            for j, char in enumerate(row):
                snake_word_chars.append((i, tly+j, char))
            i += 1

        return snake_word_chars
