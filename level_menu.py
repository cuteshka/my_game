import json
import sys

import pygame
from pygame.locals import *
import constants as SOKOBAN
from game import Game


class LevelMenu:
    def __init__(self, window):
        self.font_1 = pygame.font.Font('data/Шрифты/FreeSansBold.ttf', 80)
        self.font_2 = pygame.font.Font('data/Шрифты/FreeSansBold.ttf', 40)
        self.window = window
        self.level_screen = True
        self.levels = list(range(1, SOKOBAN.NUMBER_OF_LEVELS + 1))
        self.current_level_ind = self.levels.index(self.get_curr_level_number())
        self.start()


    def start(self):
        while self.level_screen:
            self.process_event(pygame.event.wait())
            self.render(self.window)

    def process_event(self, event):
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            # выход при нажатии ESC
            if event.key == K_ESCAPE:
                self.level_screen = False
            # если нажали > или <
            elif event.key == K_RIGHT:
                self.current_level_ind = (self.current_level_ind + 1) % len(self.levels)
            elif event.key == K_LEFT:
                self.current_level_ind = (self.current_level_ind - 1) % len(self.levels)
            elif event.key == K_RETURN:
                game = Game(self.window)
                game.last_level.save()
                game.index_level = self.levels[self.current_level_ind]
                game.load_level()
                game.start()
        if event.type == MOUSEBUTTONUP:
            self.choose_option(event.pos)



    def choose_option(self, click_pos):
        # считываем координаты мыши
        x = click_pos[0]
        y = click_pos[1]
        # если кликнули по > или <
        if x > self.plus_position[0] and x < self.plus_position[
            0] + self.plus_surface.get_width() \
                and y > SOKOBAN.WINDOW_HEIGHT / 3 and y < SOKOBAN.WINDOW_HEIGHT / 3 + self.plus_surface.get_height():
            self.current_level_ind = (self.current_level_ind + 1) % len(self.levels)
        elif x > self.minus_position[0] and x < self.minus_position[
            0] + self.minus_surface.get_width() \
                and y > SOKOBAN.WINDOW_HEIGHT / 3 and y < SOKOBAN.WINDOW_HEIGHT / 3 + self.minus_surface.get_height():
            self.current_level_ind = (self.current_level_ind - 1) % len(self.levels)
        elif x > self.choose_position[0] and x < self.choose_position[
            0] + self.choose_surface.get_width() \
                and y > SOKOBAN.WINDOW_HEIGHT / 2 and y < SOKOBAN.WINDOW_HEIGHT / 2 + self.choose_surface.get_height():
            game = Game(self.window)
            game.index_level = self.levels[self.current_level_ind]
            game.last_level.save()
            game.load_level()
            game.start()

    # загрузка картинки выбора уровня
    def render(self, window):
        self.image = pygame.image.load('data/Картинки/level_menu_background.png').convert_alpha()
        window.blit(self.image, (0, 0))

        self.number_surface = self.font_1.render(str(self.levels[self.current_level_ind]), True, SOKOBAN.RED, SOKOBAN.WHITE)
        self.number_position = ((SOKOBAN.WINDOW_WIDTH / 2) - (self.number_surface.get_width() / 2), SOKOBAN.WINDOW_HEIGHT / 3)
        window.blit(self.number_surface, self.number_position)

        self.plus_surface = self.font_1.render(">", True, SOKOBAN.BLACK, SOKOBAN.WHITE)
        self.plus_position = (
        (SOKOBAN.WINDOW_WIDTH / 2) - self.plus_surface.get_width() + 100, SOKOBAN.WINDOW_HEIGHT / 3)
        window.blit(self.plus_surface, self.plus_position)

        self.minus_surface = self.font_1.render("<", True, SOKOBAN.BLACK, SOKOBAN.WHITE)
        self.minus_position = (
            (SOKOBAN.WINDOW_WIDTH / 2) - 100, SOKOBAN.WINDOW_HEIGHT / 3)
        window.blit(self.minus_surface, self.minus_position)

        self.choose_surface = self.font_2.render("Выбрать", True, SOKOBAN.GREEN, SOKOBAN.WHITE)
        self.choose_position = (
        (SOKOBAN.WINDOW_WIDTH / 2) - (self.choose_surface.get_width() / 2), SOKOBAN.WINDOW_HEIGHT / 2)
        window.blit(self.choose_surface, self.choose_position)

        pygame.display.flip()

    def get_curr_level_number(self):
        try:
            with open("last_level", "r") as data:
                scores = json.load(data)
                return scores["level"]
        except FileNotFoundError:
            return 1