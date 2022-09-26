import pygame
from tiles import Tile
from settings import *
from player import Player


class Level:
    def __init__(self, level_data, surface):
        # sprites setup
        self.tiles = pygame.sprite.Group()
        self.player = pygame.sprite.GroupSingle()

        # level setup
        self.display_surface = surface
        self.level_data = level_data
        self.setup(level_data)
        self.world_shift = 0

    def setup(self, layout):

        for row_index, row in enumerate(layout):
            for col_index, cell in enumerate(row):
                if cell != '':
                    # calculate position only if necessary
                    x = col_index * tile_size
                    y = row_index * tile_size

                    # define tile sprites
                    if cell == 'X':
                        tile = Tile((x, y), tile_size)
                        self.tiles.add(tile)

                    # define player sprite
                    if cell == 'P':
                        player = Player((x, y))
                        self.player.add(player)

    def scroll_x(self):
        player = self.player.sprite  # player's sprite object
        player_x = player.rect.centerx      # player's x coordinate
        direction_x = player.direction.x    # player's direction movement

        # scrolling to the left
        if player_x < 200 and direction_x < 0:
            self.world_shift = 4
            player.velocity = 0
            return

        # scrolling to the right
        if player_x > 1000 and direction_x > 0:
            self.world_shift = -4
            player.velocity = 0
            return

        # default, no scrolling at all
        self.world_shift = 0
        player.velocity = 4


    def run(self):
        screen = self.display_surface

        # update and draw tiles
        self.tiles.update(self.world_shift)
        self.tiles.draw(screen)

        # update and draw player
        self.player.update()
        self.player.draw(screen)

        # update world-shift scrolling
        self.scroll_x()
