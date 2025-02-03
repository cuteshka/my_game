import pygame
from pygame import QUIT

import constants as SOKOBAN


def main():
    pygame.init()
    pygame.key.set_repeat(100, 100)
    pygame.display.set_caption("Сокобан")
    window = pygame.display.set_mode((SOKOBAN.WINDOW_WIDTH, SOKOBAN.WINDOW_HEIGHT))

    run = True
    while run:
        event = pygame.event.wait()
        if event.type == QUIT:
            run = False

        pygame.draw.rect(window, SOKOBAN.WHITE, (0, 0, SOKOBAN.WINDOW_WIDTH, SOKOBAN.WINDOW_HEIGHT))
        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    main()