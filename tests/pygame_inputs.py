#!/usr/bin/env python3

import sys
import math
import pygame
from dataclasses import dataclass

pygame.init()

clock = pygame.time.Clock()

screen = pygame.display.set_mode([300, 300])

base_font = pygame.font.Font(None, 32)
user_txt = ""

left = screen.get_width() // 2 - screen.get_width() // 4
top = screen.get_height() // 2 - screen.get_height() // 4
input_rect = pygame.Rect(left, top, 100, 100)

color = pygame.Color("white")

# width between animated characters
W_FACTOR = 20

# factor of pi to use to step between
WOBBLE_STEP = math.pi / (24)

FRAME_RATE = 24

DARK_PURPLE = (82, 28, 102)


@dataclass
class PixelPoint:
    x: int
    y: int


p1 = PixelPoint(input_rect.x, input_rect.y)


def main():
    i = 0
    while True:
        clock.tick(FRAME_RATE)

        i += 1
        if i == 1000 * FRAME_RATE:
            i = 0

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN or event.type == pygame.QUIT:
                if event.key == pygame.K_SPACE:
                    pygame.quit()
                    sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.type == pygame.K_g or event.key == ord("g"):
                    print("gooo")

        screen.fill(DARK_PURPLE)

        pygame.draw.rect(screen, DARK_PURPLE, input_rect)

        user_text = "SNAKE"

        # draw hello world a few pixels apart
        for j, letter in enumerate(user_text):
            x = p1.x + j * W_FACTOR + 3
            y = p1.y + int(12 * math.sin(0.5 * (i - j) * WOBBLE_STEP)) + 50
            text_surface = base_font.render(user_text[j], True, (255, 255, 255))
            screen.blit(text_surface, (x, y))

        input_rect.w = max(100, text_surface.get_width() + 10)
        input_rect.h = max(100, text_surface.get_height() + 10)

        pygame.display.flip()


if __name__ == "__main__":
    main()
