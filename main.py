import pygame
from pygame.locals import *

import constants as SOKOBAN
from game import Game
from menu import Menu


def main():
    # создаем окно
    pygame.init()
    # настраиваем параметры повторения нажатия клавиш
    pygame.key.set_repeat(100, 100)
    pygame.display.set_caption("Сокобан")
    window = pygame.display.set_mode((SOKOBAN.WINDOW_WIDTH, SOKOBAN.WINDOW_HEIGHT))
    menu = Menu()

    run = True
    while run:
        event = pygame.event.wait()
        if event.type == QUIT:
            run = False
        if event.type == KEYDOWN:
            if event.key == K_s:
                new_game = Game(window)
                new_game.start()
                print("игра")
            elif event.key == K_c:
                print("продолжаем")
            elif event.key == K_l:
                print("выбор уровня")
            elif event.key == K_ESCAPE:
                run = False
        if event.type == MOUSEBUTTONUP:
            run = menu.choose_option(event.pos, window)
        pygame.draw.rect(window, SOKOBAN.WHITE, (0, 0, SOKOBAN.WINDOW_WIDTH, SOKOBAN.WINDOW_HEIGHT))
        # загружаем картинку меню
        menu.render(window)
        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    main()