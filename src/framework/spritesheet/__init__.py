import pygame

import config.colors as colors


class SpriteSheet:
    def __init__(self, filename):
        self.spritesheet = pygame.image.load(filename)

    def get_image(self, x, y, width, height, xflip, yflip):
        """Get sprite from a spritesheet.

        Keyword arguments:
        x (int) -- the x coordinate where image shall be extracted
        y (int) -- the y coordinate where image shall be extracted
        width (int) -- the width of the image that shall be extracted
        height (int) -- the height of the image that shall be extracted
        xflip (bool) -- if tile needs to be flipped by x axis
        yflip (bool) -- if tile needs to be flipped by y axis

        Returns:
        image (pygame.Surface) -- sprite that was extracted
        """

        image = pygame.transform.flip(
            pygame.Surface([width, height]).convert(), xflip, yflip
        )
        image.blit(self.spritesheet, (0, 0), (x, y, width, height))
        image.set_colorkey(colors.BLACK)

        return image
