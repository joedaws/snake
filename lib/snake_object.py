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


DIRECTION_TO_OPPOSITE_DIRECTION = {
    Direction.UP: Direction.DOWN,
    Direction.DOWN: Direction.UP,
    Direction.LEFT: Direction.RIGHT,
    Direction.RIGHT: Direction.LEFT
}


class SnakeObject(TerminalDisplayObject):
    HEAD = 'X'
    BODY = '■'

    def __init__(self,
                 terminal_display: TerminalDisplay,
                 name: str = "snake",
                 initial_length: int = 2):
        # TODO load this from the config in the future
        self.initial_length = initial_length
        # should be lower depth than border but higher than food
        depth = 2

        # call be the rest of the setup
        super().__init__(name=name,
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
            i, j = self.update_i_j(i,
                                   j,
                                   DIRECTION_TO_OPPOSITE_DIRECTION[direction])
            # TODO For long inital length need to update this
            # to accomodate changing directions
            snake += [(i, j, self.BODY)]
            self.directions.append(direction)

        return snake

    def move(self, direction: Direction):
        """
        move the snake include it's body parts one unit.
        """
        # get snake head
        head_tup = self.chars[0]
        old_dir = self.directions[0]

        # if opposite direction is input, then keep going in current direction
        if old_dir == DIRECTION_TO_OPPOSITE_DIRECTION[direction]:
            direction = old_dir

        # move head to new position
        i, j, char = head_tup
        i, j = self.update_i_j(i, j, direction)
        self.head_position = (i, j)
        self.directions[0] = direction

        new_chars = [(i, j, char)]

        # update the body of the snake
        k = 1
        for d, char_tup in zip(self.directions[1:], self.chars[1:]):
            i, j, char = char_tup
            # print(f"moving {d} body part from {i} {j}")
            i, j = self.update_i_j(i, j, d)
            # print(f"                              to {i} {j}")
            self.directions[k] = direction
            new_chars.append((i, j, self.BODY))
            direction = d
            k += 1

        self.chars = new_chars

    @staticmethod
    def update_i_j(i: int, j: int, direction: Direction):
        """update the i, j according to the direction"""
        if direction == Direction.LEFT:
            j = j - 1

        elif direction == Direction.RIGHT:
            j = j + 1

        elif direction == Direction.UP:
            i = i - 1

        elif direction == Direction.DOWN:
            i = i + 1
        return i, j
