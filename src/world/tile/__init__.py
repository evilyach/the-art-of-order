import pygame

import config.colors as colors
import config.settings as settings


class Tile(pygame.sprite.Sprite):
    def __init__(self, game, x, y, texture, collidable=True):
        """Initialize a tile.

        Keyword arguments:
        x (int) -- the x coordinate where tile shall be placed
        y (int) -- the y coordinate where tile shall be placed
        width (int) -- the width of the tile shall that be placed
        height (int) -- the height of the tile shall that be placed
        texture (tuple):
          - image (pygame.Surface) -- sprite that should be placed inside tile
          - texture_x (int) -- the x coordinate of a sprite on a spritesheet
          - texture_y (int) -- the y coordinate of a sprite on a spritesheet
        collidable=True (bool) -- Can player and other entites collide with
            a tile

        This generates a tile in the world. You need to pass information about
        its position and its properties.
        """

        if collidable:
            self.groups = game.all_sprites, game.walls
        else:
            self.groups = game.all_sprites

        self.sprite_tilesize = 32
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.game = game
        self.x = x
        self.y = y

        (image, texture_x, texture_y) = texture
        self.image = self.load_texture(
            image, texture_x * self.sprite_tilesize, texture_y * self.sprite_tilesize
        )
        self.rect = self.image.get_rect()

        self.rect.x = self.x * settings.TILESIZE
        self.rect.y = self.y * settings.TILESIZE

    def load_texture(self, image, x, y):
        """ Load a texture from an image from (x, y) coordinates. """

        return pygame.transform.scale(
            image.get_image(x, y, self.sprite_tilesize, self.sprite_tilesize),
            (settings.TILESIZE, settings.TILESIZE),
        )
