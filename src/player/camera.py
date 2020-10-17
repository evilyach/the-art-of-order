import pygame

import config.settings as settings


class Camera:
    def __init__(self, width, height):
        self.width = width
        self.height = height

        self.camera = pygame.Rect(0, 0, self.width, self.height)

    def apply(self, entity):
        return entity.rect.move(self.camera.topleft)

    def update(self, target):
        x = -target.rect.x + int(settings.RESOLUTION_X / 2)
        y = -target.rect.y + int(settings.RESOLUTION_Y / 2)
        self.camera = pygame.Rect(x, y, self.width, self.height)
