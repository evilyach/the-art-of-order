import pygame

import config.colors as colors
import config.settings as settings
from framework.logger import logger


class Player(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.game = game
        self.x = x
        self.y = y

        self.image = pygame.Surface((settings.TILESIZE, settings.TILESIZE))
        self.image.fill(colors.YELLOW)
        self.rect = self.image.get_rect()

        logger.info("Created player at ({}, {})".format(self.x, self.y))

    def move(self, dx=0, dy=0):
        if not self.collide(dx, dy):
            self.x += dx
            self.y += dy

    def collide(self, dx=0, dy=0):
        for wall in self.game.walls:
            if wall.x == self.x + dx and wall.y == self.y + dy:
                return True

        return False

    def update(self):
        self.rect.x = self.x * settings.TILESIZE
        self.rect.y = self.y * settings.TILESIZE
