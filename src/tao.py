import os
import sys

import pygame

import config.colors as colors
import config.settings as settings
import config.world as world_settings
import player
import player.camera as player_camera
import world
from framework.logger import logger


class Game:
    def __init__(self):
        logger.info("Initializing game")

        pygame.init()
        pygame.display.set_caption(settings.TITLE)
        pygame.key.set_repeat(500, 80)

        self.game_folder = os.path.dirname(__file__)
        self.clock = pygame.time.Clock()
        self.fullscreen_toggle(fullscreen=True)

        self.load_data()

        logger.info("Initialized game")

    def load_data(self):
        pass

    def new(self):
        logger.info("Initializing new game objects")

        self.all_sprites = pygame.sprite.Group()
        self.walls = pygame.sprite.Group()

        self.map = world.World(self)
        self.player = player.Player(
            self, world_settings.WIDTH / 2, world_settings.HEIGHT / 2
        )
        self.camera = player_camera.Camera(self.map.width, self.map.height)

    def run(self):
        logger.info("Starting game loop")

        self.playing = True
        while self.playing:
            self.dt = self.clock.tick(settings.FPS) / 1000
            self.events()
            self.update()
            self.draw()

    def quit(self):
        logger.info("Exiting!")

        pygame.quit()
        sys.exit(0)

    def update(self):
        self.camera.update(self.player)
        self.all_sprites.update()

    def draw(self):
        self.screen.fill(pygame.Color(colors.BG_COLOR))

        for sprite in self.all_sprites:
            self.screen.blit(sprite.image, self.camera.apply(sprite))

        pygame.display.flip()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.quit()

                if event.key == pygame.K_F11:
                    if self.fullscreen:
                        self.fullscreen_toggle(fullscreen=False)
                    else:
                        self.fullscreen_toggle(fullscreen=True)

    def show_start_screen(self):
        pass

    def show_go_screen(self):
        pass

    def fullscreen_toggle(self, fullscreen=True):
        self.fullscreen = fullscreen
        if self.fullscreen:
            self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        else:
            self.screen = pygame.display.set_mode(
                (settings.RESOLUTION_X, settings.RESOLUTION_Y), pygame.RESIZABLE
            )


def main():
    game = Game()
    game.show_start_screen()

    while True:
        game.new()
        game.run()
        game.show_go_screen()


if __name__ == "__main__":
    main()
