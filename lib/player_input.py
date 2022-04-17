#!/usr/bin/env python3

from enum import Enum, auto


class DPadDirection(Enum):
    UP = auto()
    DOWN = auto()
    RIGHT = auto()
    LEFT = auto()


class InputListener:
    """
    Listens continuously to player inputs and
    updates the DPad state

    The dpad state is updated
    based on what button was pressed last.

    TODO add a pause button feature.
    """
    def __init__(self):
        self.dpad_state

    def listen(self):
        """Get player input and update DPadState"""


class PlayerAction:
    """
    communicates inputs from the
    player with objects in the game runner.
    """
