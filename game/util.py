"""
Useful utilities
"""
from dataclasses import dataclass

import pygame

from game.constants import RECT_WIDTH, RECT_HEIGHT, TITLE_FONT_SIZE


@dataclass
class PixelPoint:
    x: int
    y: int


def get_input_rect(screen, width=RECT_WIDTH, height=RECT_HEIGHT):
    left = screen.get_width() // 2 - screen.get_width() // 4
    top = screen.get_height() // 2 - screen.get_height() // 4
    input_rect = pygame.Rect(left, top, width, height)
    return input_rect


def get_title_base_font():
    base_font = pygame.font.Font(None, TITLE_FONT_SIZE)
    return base_font


class FrameCounterMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class FrameCounter(metaclass=FrameCounterMeta):
    """Get the number of frames that have passed"""

    def __init__(self):
        self.i = 0

    def increment(self):
        if self.i >= 1000:
            self.i = 0
        else:
            self.i += 1
