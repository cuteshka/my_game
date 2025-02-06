import sys

from pygame.locals import *
from game_menu import GameMenu
from level import *
from player import Player


class Game:
    def __init__(self, window):
        self.window = window
        self.load_textures()
        self.player = None
        self.index_level = 1
        self.load_level()
        self.play = True
        self.game_menu = GameMenu(self.player, self.level)

    # загружаем картинки для отрисовки в словарь
    def load_textures(self):
        self.textures = {
            SOKOBAN.WALL: pygame.image.load('data/Картинки/wall.png').convert_alpha(),
            SOKOBAN.BOX: pygame.image.load('data/Картинки/box.png').convert_alpha(),
            SOKOBAN.TARGET: pygame.image.load('data/Картинки/target.png').convert_alpha(),
            SOKOBAN.TARGET_FILLED: pygame.image.load('data/Картинки/box_on_target.png').convert_alpha(),
            SOKOBAN.PLAYER: pygame.image.load('data/Картинки/player.png').convert_alpha()
        }

    # загружаем уровень
    def load_level(self):
        self.level = Level(self.index_level)
        self.board = pygame.Surface((self.level.width, self.level.height))
        if self.player:
            self.player.pos = self.level.player_coord
            self.game_menu.level = self.level
        else:
            self.player = Player(self.level)

    def start(self):
        while self.play:
            self.process_event(pygame.event.wait())
            self.update_screen()

    # обрабатываем действия игрока
    def process_event(self, event):
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        # если нажата какая-то клавиша на клавиатуре
        if event.type == KEYDOWN:
            # выход при нажатии ESC
            if event.key == K_ESCAPE:
                self.play = False
            # если нажали одну из стрелок
            if event.key in [K_UP, K_DOWN, K_LEFT, K_RIGHT]:
                # двигаем героя
                self.player.move(event.key, self.level, self.game_menu)
                # если выиграл, переходим к следующему уровню
                # if self.has_win():
                #     self.index_level += 1
                #     self.scores.save()
                #     self.load_level()
            # перезапуск уровня
            if event.key == K_r:
                self.load_level()
            # возврат к предыдущему действию
            # if event.key == K_p:
            #     self.level.cancel_last_move(self.player, self.game_menu)
        # если отпустили кнопку мыши, то сохраняем координаты точки
        if event.type == MOUSEBUTTONUP:
            self.game_menu.click(event.pos, self.level, self)


    def update_screen(self):
        pygame.draw.rect(self.board, SOKOBAN.WHITE,
                         (0, 0, self.level.width * SOKOBAN.SPRITESIZE, self.level.height * SOKOBAN.SPRITESIZE))
        pygame.draw.rect(self.window, SOKOBAN.WHITE, (0, 0, SOKOBAN.WINDOW_WIDTH, SOKOBAN.WINDOW_HEIGHT))

        self.level.render(self.board, self.textures)
        self.player.render(self.board, self.textures)

        pox_x_board = (SOKOBAN.WINDOW_WIDTH / 2) - (self.board.get_width() / 2)
        pos_y_board = (SOKOBAN.WINDOW_HEIGHT / 2) - (self.board.get_height() / 2)
        self.window.blit(self.board, (pox_x_board, pos_y_board))

        pygame.display.flip()
