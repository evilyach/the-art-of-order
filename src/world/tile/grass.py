import pygame

import world.tile as tile


class GrassTile(tile.Tile):
    def __init__(self, game, x, y, image):
        super().__init__(game, x, y, (image, 0, 0), False)


class DarkGrassTile(tile.Tile):
    def __init__(self, game, x, y, image):
        super().__init__(game, x, y, (image, 1, 0), False)


class YellowGrassTile(tile.Tile):
    def __init__(self, game, x, y, image):
        super().__init__(game, x, y, (image, 2, 0), False)


class DuskGrassTile(tile.Tile):
    def __init__(self, game, x, y, image):
        super().__init__(game, x, y, (image, 3, 0), False)
