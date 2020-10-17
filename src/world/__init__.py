import pygame

import config.settings as settings
from framework.logger import logger


class World:
    def __init__(self, filename):
        self.filename = filename

        logger.info("Creating world from {}".format(settings.MAP_PATH))
        self.data = []

        with open(self.filename, "rt") as f:
            for line in f:
                self.data.append(line)

        if len(self.data) == 0:
            logger.error("Could not load data from from {}".format(settings.MAP_PATH))

        self.tilewidth = len(self.data[0])
        self.tileheigth = len(self.data)
        self.width = self.tilewidth * settings.TILESIZE
        self.height = self.tileheigth * settings.TILESIZE

        logger.info("Successfully created world from {}".format(settings.MAP_PATH))
