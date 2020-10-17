import pygame

import config.colors as colors
import config.player as player_settings
import config.settings as settings
from framework.logger import logger


class Player(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.game = game
        self.x = x * settings.TILESIZE
        self.y = y * settings.TILESIZE
        self.vx = 0
        self.vy = 0

        self.image = pygame.Surface((settings.TILESIZE, settings.TILESIZE))
        self.image.fill(colors.YELLOW)
        self.rect = self.image.get_rect()

        logger.info("Created player at ({}, {})".format(self.x, self.y))

    def __get_keys(self):
        self.vx = 0
        self.vy = 0

        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.vx = -player_settings.PLAYER_SPEED
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.vx = player_settings.PLAYER_SPEED
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            self.vy = -player_settings.PLAYER_SPEED
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            self.vy = player_settings.PLAYER_SPEED

        # If moving diagonally, multiply velocity for both coordinates by
        # $\frac{1}{\sqrt{2}}$, or 0.7071
        if self.vx != 0 and self.vy != 0:
            self.vx *= 0.7071
            self.vy *= 0.7071

    def collide(self, direction):
        if direction == "x":
            hits = pygame.sprite.spritecollide(self, self.game.walls, False)
            if hits:
                if self.vx > 0:
                    self.x = hits[0].rect.left - self.rect.width

                if self.vx < 0:
                    self.x = hits[0].rect.right

                self.vx = 0
                self.rect.x = self.x

        if direction == "y":
            hits = pygame.sprite.spritecollide(self, self.game.walls, False)
            if hits:
                if self.vy > 0:
                    self.y = hits[0].rect.top - self.rect.height

                if self.vy < 0:
                    self.y = hits[0].rect.bottom

                self.vy = 0
                self.rect.y = self.y

    def update(self):
        self.__get_keys()

        self.x += self.vx * self.game.dt
        self.y += self.vy * self.game.dt

        self.rect.x = self.x
        self.collide("x")
        self.rect.y = self.y
        self.collide("y")
