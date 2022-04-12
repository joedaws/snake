#!/usr/bin/env python3

from lib.terminal_display import TerminalDisplay
from lib.terminal_display_object import TerminalDisplayObject
import random
from enum import Enum


class Direction(Enum):
    """Class to represent the direction each piece is travelling."""
    UP = 0
    LEFT = 1
    RIGHT = 2
    DOWN = 3


class SnakeObject(TerminalDisplayObject):
    HEAD = 'X'
    BODY = '■'

    def __init__(self,
                 terminal_display: TerminalDisplay,
                 initial_length: int = 2):
        # TODO load this from the config in the future
        self.initial_length = initial_length
        # should be lower depth than border but higher than food
        depth = 2

        # call be the rest of the setup
        super().__init__(name="snake",
                         depth=depth,
                         terminal_display=terminal_display)

        td = self.terminal_display

        # random starting direction
        self.directions = [Direction(random.randint(0, 3))]

        # inital head position is somewhere in the middle
        self.head_position = (td.rows // 2, td.columns // 2)

        # call only after head position and direction are set
        self.chars = self._setup_snake_chars()

    def _setup_snake_chars(self):
        """Create the head and body of the snake."""
        # TODO fill in to make sure adding new pieces is valid
        i, j = self.head_position
        snake = [(i, j, self.HEAD)]

        # adding body pieces in the opposite direction
        direction = self.directions[0]
        for _ in range(self.initial_length):
            if direction == Direction.LEFT:
                j = j + 1

            elif direction == Direction.RIGHT:
                j = j - 1

            elif direction == Direction.UP:
                i = i - 1

            elif direction == Direction.DOWN:
                i = i + 1

            # TODO For long inital length need to update this
            # to accomodate changing directions
            snake += [(i, j, self.BODY)]
            self.directions.append(direction)

        return snake
