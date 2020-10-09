import pygame

import config.colors as colors
import config.settings as settings


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

    def move(self, dx=0, dy=0):
        self.x += dx
        self.y += dy

    def update(self):
        self.rect.x = self.x * settings.TILESIZE
        self.rect.y = self.y * settings.TILESIZE
