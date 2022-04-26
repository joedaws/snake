#!/usr/bin/env python3

import sys
import time
import pygame

pygame.init()

clock = pygame.time.Clock()

screen = pygame.display.set_mode([600,500])

base_font = pygame.font.Font(None, 32)
user_txt = ''

input_rect = pygame.Rect(200, 200, 140, 32)

color = pygame.Color('lightskyblue3')

def main():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pygame.quit()
                    sys.exit()

        screen.fill((255, 255, 255))

        pygame.draw.rect(screen, color, input_rect)

        user_text = "Hello"

        text_surface = base_font.render(user_text,
                                        True,
                                        (255, 255, 255))

        screen.blit(text_surface, (input_rect.x+5, input_rect.y+5))

        input_rect.w = max(100, text_surface.get_width()+10)

        pygame.display.flip()

        clock.tick(60)

if __name__ == "__main__":
    main()
