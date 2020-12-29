import pygame

import world.tile as tile


class StoneBrickWhiteTile(tile.Tile):
    def __init__(self, game, x, y, image):
        super().__init__(game, x, y, (image, 0, 31), True)
