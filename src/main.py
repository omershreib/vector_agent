import pygame, sys
from settings import *
from level import Level

#
background_color = (37, 113, 121)

# pygame setup
pygame.init()
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()
level = Level(level_map, screen)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill(background_color)
    level.run()

    pygame.display.update()
    clock.tick(60)