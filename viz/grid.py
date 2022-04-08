#!/usr/bin/env python3

from typing import List, Tuple
import random
import time
import os
import sys


BLANK_CHAR = ' '
WALL_CHAR = '│'
UPPER_RIGHT_CHAR = '┐'
LOWER_RIGHT_CHAR = '┘'
LOWER_LEFT_CHAR = '└'
UPPER_LEFT_CHAR = '┌'
BOX_HORIZONTAL_CHAR = '─'


class Grid:
    """
    class for holding the grid

    has a method to place a character
    """
    def __init__(self, rows: int = 10, columns: int = 40):
        self.rows = rows
        self.columns = columns
        self.chars = get_blank_grid(self.rows, self.columns)
        self.hash_to_object = {}

    def place_in_chars(self, i: int, j: int, char: str):
        """
        place a char in the grid if it doesn't not already exist.
        """
        # check valid input
        if len(char) != 1:
            raise ValueError("update_chars expects single character not list")

        # ensure that no objects collide
        for obj_hash in self.hash_to_object:
            exist_i, exist_j, exist_char = self.hash_to_object.get(obj_hash)
            if exist_i == i and exist_j == j:
                raise ValueError(f"Cannot place {char} in position {i} {j} "
                                 f"since {exist_char} is already there.")

        # place object in the map of objects
        obj = (i, j, char)
        self.hash_to_object[get_obj_hash(obj)] = obj

        # make adjustments so that the char is appropriately placed.
        adjusted_i, adjusted_j = get_grid_chars_index(i, j)

        self.chars[adjusted_i][adjusted_j] = char

    def move_object(self, obj_hash: str, vert: int, hori: int):
        """
        moves an existing object

        move it vert units up (or down if negative)
        and move it hori units right (or left if negative)
        """
        obj = self.hash_to_object.get(obj_hash)
        if obj:
            # remove old obj from hash_to_object
            i, j, char = self.hash_to_object.pop(obj_hash)
            # replace char with blank
            adjusted_i, adjusted_j = get_grid_chars_index(i, j)

            self.chars[adjusted_i][adjusted_j] = BLANK_CHAR

            valid_i, valid_j = self._valid_position(i+vert, j+hori)

            self.place_in_chars(valid_i, valid_j, char)

        else:
            raise ValueError(f"move_object was passed a hash that was"
                             "not registred. It was {obj_hash}")

    def _valid_position(self, i: int, j: int) -> Tuple[int, int]:
        """returns a valid position."""
        if i >= self.rows:
            i = self.rows - 1
        elif i < 0:
            i = 0

        if j >= self.columns:
            j = self.columns - 1
        elif j < 0:
            j = 0

        return i, j

    def __str__(self):
        return draw(self.chars)


def get_obj_hash(obj: Tuple[int, int, str]):
    """
    The input obj needs to be hashed
    """
    return f"{obj[0]}{obj[1]}{obj[2]}"


def get_blank_grid(n: int = 10, m: int = 40):
    """
    n is number of rows
    m is number of columns

    the grid is bounded by boarder
    """
    top_boarder = [UPPER_LEFT_CHAR] + [BOX_HORIZONTAL_CHAR] * m + [UPPER_RIGHT_CHAR]
    bottom_boarder = [LOWER_LEFT_CHAR] + [BOX_HORIZONTAL_CHAR] * m + [LOWER_RIGHT_CHAR]

    grid = [top_boarder]
    for i in range(n):
        this_row = []
        this_row = [WALL_CHAR] + [BLANK_CHAR] * m + [WALL_CHAR]
        grid.append(this_row)
    grid.append(bottom_boarder)

    return grid


def draw(grid: List[List[str]]) -> str:
    out_str = ""
    for row in grid:
        for char in row:
            out_str += char
        out_str += '\n'
    return out_str


def get_grid_chars_index(i: int, j: int):
    """
    the input i and j are between the original nxm array.
    The output i and j are translated to the indices of grid.chars
    """
    return i + 1, j + 1


if __name__ == "__main__":
    game_grid = Grid()
    #print(game_grid)
    # place an X at top left
    game_grid.place_in_chars(0, 0, 'X')
    #print(game_grid)

    #print(game_grid.hash_to_object)

    # place an x somewhere in the middle
    obj_hash = get_obj_hash((0, 0, 'X'))
    #print(obj_hash)
    game_grid.move_object(obj_hash, 0, 1)
    #print(game_grid)

    directions = {'up': (1, 0),
                  'down': (-1, 0),
                  'left': (0, -1),
                  'right': (0, 1)}

    nlines = len(game_grid.chars)
    # scroll up to make room for output
    print(f"\033[{nlines}S", end="")

    # move cursor back up
    print(f"\033[{nlines}A", end="")

    # save current cursor position
    print("\033[s", end="")

    for _ in range(1000):
        # restore saved cursor position
        print("\033[u", end="")

        # update the random direction
        vert, hori = directions[random.choice(list(directions))]
        obj_hash = list(game_grid.hash_to_object.keys())[0]
        game_grid.move_object(obj_hash, vert, hori)
        print(game_grid)
        time.sleep(0.1)
