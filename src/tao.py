import pygame
import pygame.locals
import sys
from config.textures import Textures
from config.common import Settings


def main():
    pygame.init()
    clock = pygame.time.Clock()

    screen = pygame.display.set_mode((800, 600))
    screen.fill((255, 255, 255))

    done = False

    while not done:
        clock.tick(Settings["fps"])

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        pygame.display.update()


if __name__ == "__main__":
    main()
