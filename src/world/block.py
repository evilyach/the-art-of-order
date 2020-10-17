import pygame

import config.colors as colors
import config.settings as settings


class Block(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.walls
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.game = game
        self.x = x
        self.y = y

        self.image = pygame.Surface((settings.TILESIZE, settings.TILESIZE))
        self.image.fill(colors.GREEN)
        self.rect = self.image.get_rect()

        self.rect.x = self.x * settings.TILESIZE
        self.rect.y = self.y * settings.TILESIZE
