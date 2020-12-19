import pygame

import config.colors as colors
import config.player as player_settings
import config.settings as settings
from framework.logger import logger
from framework.spritesheet import SpriteSheet


class Player(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.game = game
        self.x = x * settings.TILESIZE
        self.y = y * settings.TILESIZE
        self.vx = 0
        self.vy = 0

        filename = "src/static/sprites/character.png"
        try:
            self.load_textures(filename)
        except FileNotFoundError as error:
            logger.error(f"Could not find character spritesheet at {filename}")
            exit(-1)

        self.image = self.move_down_textures[0]
        self.rect = self.image.get_rect()

        logger.info("Created player at ({}, {})".format(self.x, self.y))

    def load_textures(self, filename):
        """Load texture set for a character from a filename.

        Keyword arguments:
        filename (str) -- path to the file, which we load textures from

        Right now the character spritesheet looks like 4 x 4 tileset. We
        extract 4 sprites for each movement direction.
        """

        image = SpriteSheet(filename)

        self.move_down_textures = []
        for x in range(0, 64, 16):
            sprite = pygame.transform.scale(
                image.get_image(x, 0, 16, 16), (settings.TILESIZE, settings.TILESIZE)
            )
            self.move_down_textures.append(sprite)

        self.move_left_textures = []
        for x in range(0, 64, 16):
            sprite = pygame.transform.scale(
                image.get_image(x, 16, 16, 16), (settings.TILESIZE, settings.TILESIZE)
            )
            self.move_left_textures.append(sprite)

        self.move_up_textures = []
        for x in range(0, 64, 16):
            sprite = pygame.transform.scale(
                image.get_image(x, 32, 16, 16), (settings.TILESIZE, settings.TILESIZE)
            )
            self.move_up_textures.append(sprite)

        self.move_right_textures = []
        for x in range(0, 64, 16):
            sprite = pygame.transform.scale(
                image.get_image(x, 48, 16, 16), (settings.TILESIZE, settings.TILESIZE)
            )
            self.move_right_textures.append(sprite)

    def move(self):
        keys = pygame.key.get_pressed()

        left_keys = keys[pygame.K_LEFT] or keys[pygame.K_a]
        right_keys = keys[pygame.K_RIGHT] or keys[pygame.K_d]
        up_keys = keys[pygame.K_UP] or keys[pygame.K_w]
        down_keys = keys[pygame.K_DOWN] or keys[pygame.K_s]

        # If inertia is present, don't just zero out velocities
        if player_settings.INERTIA:
            self.vx *= player_settings.INERTIA_COEFFICIENT
            self.vy *= player_settings.INERTIA_COEFFICIENT
        else:
            self.vx = 0
            self.vy = 0

        if left_keys:
            self.vx = -player_settings.PLAYER_SPEED
        if right_keys:
            self.vx = player_settings.PLAYER_SPEED
        if up_keys:
            self.vy = -player_settings.PLAYER_SPEED
        if down_keys:
            self.vy = player_settings.PLAYER_SPEED

        # If moving diagonally, multiply velocity for both coordinates by
        # $\frac{1}{\sqrt{2}}$, or 0.7071
        if (
            (down_keys and left_keys)
            or (down_keys and right_keys)
            or (up_keys and left_keys)
            or (up_keys and right_keys)
        ):
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
        self.move()

        self.x += self.vx * self.game.dt
        self.y += self.vy * self.game.dt

        # Update textures
        if self.vy > 0:
            frame = (int(self.y) // 30) % len(self.move_down_textures)
            self.image = self.move_down_textures[frame]
        elif self.vy < 0:
            frame = (int(self.y) // 30) % len(self.move_up_textures)
            self.image = self.move_up_textures[frame]

        if self.vx > 0:
            frame = (int(self.x) // 30) % len(self.move_right_textures)
            self.image = self.move_right_textures[frame]
        elif self.vx < 0:
            frame = (int(self.x) // 30) % len(self.move_left_textures)
            self.image = self.move_left_textures[frame]

        self.rect.x = self.x
        self.collide("x")
        self.rect.y = self.y
        self.collide("y")
