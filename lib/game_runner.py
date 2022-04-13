#!/usr/bin/env python3
import sys
import time
from enum import Enum, auto
from lib.terminal_display import TerminalDisplay
from lib.snake_object import SnakeObject, Direction
from lib.display_border import Border
from lib.start_up_screen import StartUpScreen


directions = [Direction.UP]*3 +\
        [Direction.RIGHT]*2 +\
        [Direction.DOWN]*2 +\
        [Direction.LEFT]*2


class GameState(Enum):
    """
    class for storing the different states a game can be in
    """
    START_UP = auto()
    SPLASH_SCREEN = auto()
    PLAY = auto()
    PAUSE = auto()
    GAMEOVER = auto()


class GameRunner:
    """
    This is the class that is responsible for running the game
    by coordianting updates of objects and updates to the terminal
    display object.

    LEVEL_UP_IT is the iteration number in the loop method on which we
    increment the level.
    """
    LEVEL_UP_IT = 100
    def __init__(self, config=None):
        """
        TODO fill in the config
        """
        self.config = config

        self.td = TerminalDisplay()
        self.objs = {
            "border": Border(self.td),
            "snake": SnakeObject(self.td),
            "start_up": StartUpScreen(self.td)
        }
        self.td.add_object(self.objs["start_up"])

        # start the game in start up phase
        self.state = GameState.START_UP
        self.running = True

        # level controls how fast things move
        self.level = 0

        # iterator for number of frames
        self.it = 0

        self.game_state_to_function = {
            GameState.START_UP: self.start_up,
            GameState.PLAY: self.play,
            GameState.GAMEOVER: self.game_over
        }

        # this seems like a good starting speed
        self.time_between_frames = 0.17

    def loop(self):
        nlines = self.td.rows + 1

        # scroll up to make room for output
        print(f"\033[{nlines}S", end="")

        # move cursor back up
        print(f"\033[{nlines}A", end="")

        # save current cursor position
        print("\033[s", end="")

        # this is a level count which tells us when to increment the level
        while self.running:
            # restore saved cursor position
            print("\033[u", end="")

            print(self.td)

            # load and call appropriate game function
            it_fun = self.game_state_to_function[self.state]
            it_fun()

            # increment the counter and level up if necessary
            if self.it > self.LEVEL_UP_IT:
                self.it = 0
                self.level += 1

            # sleep for a duration
            time.sleep(self.time_between_frames)

    def start_up(self):
        self.time_between_frames = 1.5
        self.state = GameState.PLAY
        # remove start up screen
        self.td.remove_object("start_up")

        # get ready for play state
        self.td.add_object(self.objs["border"])
        self.td.add_object(self.objs["snake"])

    def play(self):
        self.time_between_frames = 0.17
        # get inputs
        num_dir = len(directions)
        new_dir = directions[self.it % num_dir]

        # move objects
        snake = self.td.remove_object("snake")
        snake.move(new_dir)

        # check collisions
        for obj_name, obj in self.td.name_to_object.items():
            for char_tup in obj.chars:
                i, j, _ = char_tup
                if i == snake.head_position[0] and j == snake.head_position[1]:
                    if obj_name == "border":
                        self.state = GameState.GAMEOVER

        # if no collisions update as normal
        self.td.add_object(snake)

    def game_over(self):
        # TODO fill in with list of different end messages
        print("Too Bad!")
        time.sleep(1)
        sys.exit("game over")
