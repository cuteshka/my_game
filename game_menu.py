import pygame
import constants as SOKOBAN

class GameMenu:
    def __init__(self, player, level):
        self.player = player
        self.level = level
        self.font_menu = pygame.font.Font('data/Шрифты/FreeSansBold.ttf', 18)
        self.txtLevel = "Уровень " + str(level)
        self.colorTxtLevel = SOKOBAN.BLACK
        self.txtCancel = "Отменить последний ход"
        self.colorTxtCancel = SOKOBAN.GREY
        self.txtReset = "Начать уровень заново"
        self.colorTxtReset = SOKOBAN.BLACK

    def click(self, pos_click, level, game):
        # координаты нажатия кнопки мыши
        x = pos_click[0]
        y = pos_click[1]

        # обрабатываем клик на отмену хода
        if x > self.posTxtCancel[0] and x < self.posTxtCancel[0] + self.txtCancelSurface.get_width() \
         and y > self.posTxtCancel[1] and y < self.posTxtCancel[1] + self.txtCancelSurface.get_height():
            level.cancel_last_move(self.player, self)
            self.colorTxtCancel = SOKOBAN.GREY

        # обрабатываем клик на перезапуск уровня
        if x > self.posTxtReset[0] and x < self.posTxtReset[0] + self.txtResetSurface.get_width() \
        and y > self.posTxtReset[1] and y < self.posTxtReset[1] + self.txtResetSurface.get_height():
            game.load_level()

    # отображаем текст на экране
    def render(self, window, level):
        self.txtLevel = "Уровень " + str(level)
        self.txtLevelSurface = self.font_menu.render(self.txtLevel, True, self.colorTxtLevel, SOKOBAN.WHITE)
        window.blit(self.txtLevelSurface, (10, 10))

        self.txtCancelSurface = self.font_menu.render(self.txtCancel, True, self.colorTxtCancel, SOKOBAN.WHITE)
        self.posTxtCancel = (SOKOBAN.WINDOW_WIDTH - self.txtCancelSurface.get_width() - 10, 10)
        window.blit(self.txtCancelSurface, self.posTxtCancel)

        self.txtResetSurface = self.font_menu.render(self.txtReset, True, self.colorTxtReset, SOKOBAN.WHITE)
        self.posTxtReset = ((SOKOBAN.WINDOW_WIDTH / 2) - (self.txtResetSurface.get_width() / 2), 10)
        window.blit(self.txtResetSurface, self.posTxtReset)
