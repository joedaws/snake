#!/usr/bin/env python3

import sys
import pygame
from game.constants import FRAME_RATE
from game.title import title_screen
from game.play import play_screen
from game.util import FrameCounter
from game.game_state import GameState

pygame.init()

clock = pygame.time.Clock()

screen = pygame.display.set_mode([300, 300])


def main():
    game_state = GameState.TITLE
    while True:
        FrameCounter().increment()
        clock.tick(FRAME_RATE)

        # check input -----------------------------------------------------------------
        user_input = "chill"
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN or event.type == pygame.QUIT:
                if event.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_g or event.key == ord("g"):
                    user_input = "GO"

        # Different screens for different modes
        if game_state == GameState.TITLE:
            game_state = title_screen(screen, user_input)
        if game_state == GameState.PLAY:
            game_state = play_screen(screen)

        pygame.display.flip()


if __name__ == "__main__":
    main()
