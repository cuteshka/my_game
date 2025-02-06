import pygame
import constants as SOKOBAN
from game import Game


class StartMenu:
    def __init__(self):
        # загружаем фон стартового окна
        self.image = pygame.image.load('data/Картинки/start_pict.png').convert_alpha()
        # сохраняем в переменные текст меню
        self.new_game_txt = "Новая игра"
        self.continue_game_txt = "Продолжить"
        self.choose_level_txt = "Выбрать уровень"
        self.quit_game_txt = "Выйти"
        self.font = pygame.font.Font('data/Шрифты/FreeSansBold.ttf', 30)

    def choose_option(self, click_pos, window):
        # считываем координаты мыши
        x = click_pos[0]
        y = click_pos[1]
        # если кликнули по пункту меню
        if x > self.new_game_txt_position[0] and x < self.new_game_txt_position[
            0] + self.new_game_txt_surface.get_width() \
                and y > 130 and y < 130 + self.new_game_txt_surface.get_height():
            new_game = Game(window)
            new_game.start()
            print("играем")
        elif x > self.choose_level_txt_position[0] and x < self.choose_level_txt_position[
            0] + self.choose_level_txt_surface.get_width() \
                and y > 200 and y < 200 + self.choose_level_txt_surface.get_height():
            print("выбор уровня")
        elif x > self.continue_game_txt_position[0] and x < self.continue_game_txt_position[
            0] + self.continue_game_txt_surface.get_width() \
                and y > 270 and y < 270 + self.continue_game_txt_surface.get_height():
            print("продолжаем")
        elif x > self.quit_game_txt_position[0] and x < self.quit_game_txt_position[
            0] + self.quit_game_txt_surface.get_width() \
                and y > 340 and y < 340 + self.quit_game_txt_surface.get_height():
            return False

        return True

    # загрузка картинки стартового окна
    def render(self, window):
        # загружаем фон, указывая координаты верхнего левого угла
        window.blit(self.image, (0, 0))

        # преобразуем текст в изображение с использованием сглаживания (antialias)
        self.new_game_txt_surface = self.font.render(self.new_game_txt, True, SOKOBAN.BLACK, SOKOBAN.WHITE)
        # определяем координаты для размещения текста
        self.new_game_txt_position = ((SOKOBAN.WINDOW_WIDTH / 4) - (self.new_game_txt_surface.get_width() / 2), 130)
        # размещаем картинку с текстом в окне
        window.blit(self.new_game_txt_surface, self.new_game_txt_position)

        self.choose_level_txt_surface = self.font.render(self.choose_level_txt, True, SOKOBAN.BLACK, SOKOBAN.WHITE)
        self.choose_level_txt_position = (
        (SOKOBAN.WINDOW_WIDTH / 4) - (self.choose_level_txt_surface.get_width() / 2), 200)
        window.blit(self.choose_level_txt_surface, self.choose_level_txt_position)

        self.continue_game_txt_surface = self.font.render(self.continue_game_txt, True, SOKOBAN.BLACK, SOKOBAN.WHITE)
        self.continue_game_txt_position = ((SOKOBAN.WINDOW_WIDTH / 4) - (self.continue_game_txt_surface.get_width() / 2), 270)
        window.blit(self.continue_game_txt_surface, self.continue_game_txt_position)

        self.quit_game_txt_surface = self.font.render(self.quit_game_txt, True, SOKOBAN.BLACK, SOKOBAN.WHITE)
        self.quit_game_txt_position = ((SOKOBAN.WINDOW_WIDTH / 4) - (self.quit_game_txt_surface.get_width() / 2), 340)
        window.blit(self.quit_game_txt_surface, self.quit_game_txt_position)