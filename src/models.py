from pygame.sprite import Sprite as pg
from settings import *
import pygame

class Tile(pg):
    def __init__(self, x, y, size):
        super().__init__()

        # define tile surface
        self.image = pygame.Surface((size,size))
        self.image.set_colorkey(COLOR_RED)
        self.rect = self.rect = self.image.get_rect(topleft = (x,y))

    def update(self, shift):
        self.rect.x += shift




