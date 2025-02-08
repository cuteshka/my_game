import os

import pygame

import constants as SOKOBAN


class Level:
    def __init__(self, level_to_load):
        self.last_structure_state = None
        self.exist = self.has_level(level_to_load)
        if self.exist:
            self.load(level_to_load)

    # проверка, что есть такой уровень
    def has_level(self, level):
        if os.path.exists("data/Уровни/level_" + str(level) + ".txt"):
            return True
        return False

    # загрузка уровня
    def load(self, level):
        # считываем карту и преобразуем ее в более удобный для нас вид
        with open("data/Уровни/level_" + str(level) + ".txt") as level_file:
            self.structure = [list(i) for i in level_file.read().split('\n')]
            # определяем максимальную ширину ряда
            max_width = 0
            for y in range(len(self.structure)):
                if len(self.structure[y]) > max_width:
                    max_width = len(self.structure[y])
                    # запоминаем координаты игрока и удаляем их с поля
                for x in range(len(self.structure[y])):
                    if self.structure[y][x] == '@':
                        self.player_coord = [x, y]
                        self.structure[y][x] = " "
            # определяем размер поля в пикселях
            self.width = max_width * SOKOBAN.SPRITESIZE
            self.height = (len(self.structure) - 1) * SOKOBAN.SPRITESIZE

    def render(self, window, textures):
        for y in range(len(self.structure)):
            for x in range(len(self.structure[y])):
                if self.structure[y][x] in textures:
                    window.blit(textures[self.structure[y][x]], (x * SOKOBAN.SPRITESIZE, y * SOKOBAN.SPRITESIZE))
                else:
                    if self.structure[y][x] == SOKOBAN.TARGET_FILLED:
                        pygame.draw.rect(window, (0, 255, 0), (
                            x * SOKOBAN.SPRITESIZE, y * SOKOBAN.SPRITESIZE, SOKOBAN.SPRITESIZE, SOKOBAN.SPRITESIZE))
                    else:
                        pygame.draw.rect(window, SOKOBAN.WHITE, (
                            x * SOKOBAN.SPRITESIZE, y * SOKOBAN.SPRITESIZE, SOKOBAN.SPRITESIZE, SOKOBAN.SPRITESIZE))

    def cancel_last_move(self, player, interface):
        if self.last_structure_state:
            self.structure = self.last_structure_state
            player.pos = self.last_player_pos
            interface.colorTxtCancel = SOKOBAN.GREY
            self.last_structure_state = None
