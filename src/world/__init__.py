import pygame

import config.settings as settings
import config.world as world_settings
import player
import world.tile.grass as grass_tile
import world.tile.stone_brick as stone_brick_tile
from framework.logger import logger
from framework.spritesheet import SpriteSheet


class World:
    def __init__(self, game):
        self.game = game
        self.width = world_settings.WIDTH * settings.TILESIZE
        self.height = world_settings.HEIGHT * settings.TILESIZE

        self.generate()

    def generate(self):
        """ Generates world with different tile objects. """

        image = SpriteSheet("src/static/sprites/spritesheet.png")

        # Fill world with grass
        for x in range(world_settings.WIDTH):
            for y in range(world_settings.HEIGHT):
                grass_tile.DuskGrassTile(self.game, x, y, image)

        # Create unescapable border
        for x in range(world_settings.WIDTH + 1):
            stone_brick_tile.StoneBrickWhiteTile(self.game, x, 0, image)
            stone_brick_tile.StoneBrickWhiteTile(
                self.game, x, world_settings.HEIGHT, image
            )
        for y in range(world_settings.HEIGHT + 1):
            stone_brick_tile.StoneBrickWhiteTile(self.game, 0, y, image)
            stone_brick_tile.StoneBrickWhiteTile(
                self.game, world_settings.WIDTH, y, image
            )
