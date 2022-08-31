"""
Defines constants useful for the game
"""
import math

__all__ = [
    "TITLE_BG_COLOR",
    "RECT_WIDTH",
    "RECT_HEIGHT",
    "WOBBLE_STEP",
    "TITLE_FONT_SIZE",
]

TITLE_BG_COLOR = (82, 28, 102)

RECT_WIDTH = 200
RECT_HEIGHT = 100

WOBBLE_STEP = math.pi / (24)

# width between animated characters
W_FACTOR = 20

# factor of pi to use to step between
FRAME_RATE = 24

# size of font for title
TITLE_FONT_SIZE = 32
