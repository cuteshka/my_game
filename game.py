import sys

import pygame

from level import *


class Game:
    def __init__(self, window):
        self.window = window
        self.load_textures()
        self.player = None
        self.index_level = 1
        self.load_level()
        self.play = True

    # загружаем картинки для отрисовки в словарь
    def load_textures(self):
        self.textures = {
            SOKOBAN.WALL: pygame.image.load('data/Картинки/wall.png').convert_alpha(),
            SOKOBAN.BOX: pygame.image.load('data/Картинки/box.png').convert_alpha(),
            SOKOBAN.TARGET: pygame.image.load('data/Картинки/target.png').convert_alpha(),
            SOKOBAN.TARGET_FILLED: pygame.image.load('data/Картинки/box_on_target.png').convert_alpha(),
            SOKOBAN.PLAYER: pygame.image.load('data/Картинки/player.png').convert_alpha()
        }

    def start(self):
        while self.play:
            self.update_screen()

    # загружаем уровень
    def load_level(self):
        self.level = Level(self.index_level)
        self.board = pygame.Surface((self.level.width, self.level.height))

    def update_screen(self):
        pygame.draw.rect(self.board, SOKOBAN.WHITE,
                         (0, 0, self.level.width * SOKOBAN.SPRITESIZE, self.level.height * SOKOBAN.SPRITESIZE))
        pygame.draw.rect(self.window, SOKOBAN.WHITE, (0, 0, SOKOBAN.WINDOW_WIDTH, SOKOBAN.WINDOW_HEIGHT))
        self.level.render(self.board, self.textures)

        pox_x_board = (SOKOBAN.WINDOW_WIDTH / 2) - (self.board.get_width() / 2)
        pos_y_board = (SOKOBAN.WINDOW_HEIGHT / 2) - (self.board.get_height() / 2)
        self.window.blit(self.board, (pox_x_board, pos_y_board))

        pygame.display.flip()
