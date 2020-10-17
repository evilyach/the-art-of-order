import pygame

import config.player as player_settings
import config.settings as settings
from framework.logger import logger


class Camera:
    def __init__(self, width, height):
        self.width = width
        self.height = height

        self.camera = pygame.Rect(0, 0, self.width, self.height)

        logger.info(
            "Option to limit camera scrolling to map size is {}".format(
                "on" if player_settings.LIMIT_SCROLLING_TO_MAP_SIZE else "off"
            )
        )
        logger.info("Created camera for player")

    def apply(self, entity):
        return entity.rect.move(self.camera.topleft)

    def update(self, target):
        x = -target.rect.x + int(settings.RESOLUTION_X / 2)
        y = -target.rect.y + int(settings.RESOLUTION_Y / 2)

        # If we want to stop scrolling once we hit border of the map, we need
        # apply some more math to the coordinate calculation
        if player_settings.LIMIT_SCROLLING_TO_MAP_SIZE:
            # Make sure coordinates are not less than 0 for left and top of the
            # map
            x = min(0, x)  # left
            y = min(0, y)  # top

            # Make sure coordinates are not larger than width and height for
            # right and bottom of the map
            x = max(settings.RESOLUTION_X - self.width, x)  # right
            y = max(settings.RESOLUTION_Y - self.height, y)  # bottom

        self.camera = pygame.Rect(x, y, self.width, self.height)
