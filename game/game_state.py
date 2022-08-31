"""
defines the game states
"""
from enum import Enum


class GameState(Enum):
    """
    This determines what kind of screen to display
    """

    TITLE = "title"
    PAUSE = "pause"
    PLAY = "play"
