#!/usr/bin/env python3

from enum import Enum, auto


class PlayerInput(Enum):
    UP = auto()
    DOWN = auto()
    RIGHT = auto()
    LEFT = auto()
    SELECT = auto()
    PAUSE = auto()


class InputListener:
    """
    Listens continuously to player inputs and
    updates the DPad state

    The dpad state is updated
    based on what button was pressed last.

    TODO add a pause button feature.
    """
    def __init__(self):
        self.dpad_state = None

        # TODO use strategy design pattern to
        #    allow for different user input
        #    configurations

    def listen(self):
        """Get player input and update DPadState"""
        # TODO read about to continuously get user input
        player_input = None
        if player_input == 'w':
            self.dpad_state = PlayerInput.UP
        if player_input == 's':
            self.dpad_state = PlayerInput.DOWN
        if player_input == 'a':
            self.dpad_state = PlayerInput.LEFT
        if player_input == 'd':
            self.dpad_state = PlayerInput.RIGHT


class PlayerAction:
    """
    communicates inputs from the
    player with objects in the game runner.
    """
