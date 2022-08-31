"""
Title screen of the game
"""
import math
import pygame
from game.constants import TITLE_BG_COLOR, W_FACTOR, WOBBLE_STEP
from game.game_state import GameState
from game.util import get_input_rect, get_title_base_font, PixelPoint, FrameCounter


def title_screen(screen, user_input):
    i = FrameCounter().i

    screen.fill(TITLE_BG_COLOR)

    base_font = get_title_base_font()
    input_rect = get_input_rect(screen)
    p1 = PixelPoint(input_rect.x, input_rect.y)
    pygame.draw.rect(screen, TITLE_BG_COLOR, input_rect)

    title_word = "SNAKE"

    # draw hello world a few pixels apart
    for j, letter in enumerate(title_word):
        x = p1.x + j * W_FACTOR + 3
        y = p1.y + int(12 * math.sin(0.5 * (i - j) * WOBBLE_STEP)) + 50
        text_surface = base_font.render(title_word[j], True, (255, 255, 255))
        screen.blit(text_surface, (x, y))

    input_rect.w = max(100, text_surface.get_width() + 10)
    input_rect.h = max(100, text_surface.get_height() + 10)

    game_state = GameState.TITLE
    if user_input == "GO":
        game_state = GameState.PLAY

    return game_state
