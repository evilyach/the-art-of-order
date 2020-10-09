import os
import sys

import pygame

import config.colors as colors
import config.settings as settings
import player
import world


class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(settings.TITLE)
        pygame.key.set_repeat(500, 80)

        self.clock = pygame.time.Clock()
        self.screen = screen = pygame.display.set_mode(
            (settings.RESOLUTION_X, settings.RESOLUTION_Y)
        )
        self.load_data()

    def load_data(self):
        self.map_data = []
        game_folder = os.path.dirname(__file__)
        with open(os.path.join(game_folder, settings.MAP_PATH), "rt") as f:
            for line in f:
                self.map_data.append(line)

    def new(self):
        self.all_sprites = pygame.sprite.Group()
        self.walls = pygame.sprite.Group()

        self.player = player.Player(self, 1, 1)
        for row, tiles in enumerate(self.map_data):
            for col, tile in enumerate(tiles):
                if tile == "l":
                    world.Block(self, col, row)

    def run(self):
        self.playing = True
        while self.playing:
            self.dt = self.clock.tick(settings.FPS) / 1000
            self.events()
            self.update()
            self.draw()

    def quit(self):
        pygame.quit()
        sys.exit()

    def update(self):
        self.all_sprites.update()

    def draw_grid(self):
        for x in range(0, settings.RESOLUTION_X, settings.TILESIZE):
            pygame.draw.line(
                self.screen, colors.LIGHTGRAY, (x, 0), (x, settings.RESOLUTION_Y)
            )

        for y in range(0, settings.RESOLUTION_Y, settings.TILESIZE):
            pygame.draw.line(
                self.screen, colors.LIGHTGRAY, (0, y), (settings.RESOLUTION_X, y)
            )

    def draw(self):
        self.screen.fill(pygame.Color(colors.BG_COLOR))
        self.draw_grid()
        self.all_sprites.draw(self.screen)
        pygame.display.flip()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.quit()

                if event.key == pygame.K_LEFT:
                    self.player.move(dx=-1)

                if event.key == pygame.K_RIGHT:
                    self.player.move(dx=1)

                if event.key == pygame.K_UP:
                    self.player.move(dy=-1)

                if event.key == pygame.K_DOWN:
                    self.player.move(dy=1)

    def show_start_screen(self):
        pass

    def show_go_screen(self):
        pass


def main():
    game = Game()
    game.show_start_screen()

    while True:
        game.new()
        game.run()
        game.show_go_screen()


if __name__ == "__main__":
    main()
