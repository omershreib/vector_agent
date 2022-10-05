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

    def hor_movemenet_collision(self):
        player = self.player.sprite
        player.rect.x += player.direction.x * player.velocity

        for tile in self.tiles.sprites():

            # checks if the player is collide with                                  # did we have a collision?
            # one of the tile's rectangle
            if tile.rect.colliderect(player.rect):                                  # if so, where (left or right)?
                if player.direction.x < 0:      # player is moving to the left
                    player.rect.left = tile.rect.right

                elif player.direction.x > 0:      # player is moving to the right
                    player.rect.right = tile.rect.left

    def ver_movement_collision(self):
        player = self.player.sprite
        player.apply_gravity()
        player.rect.y += player.direction.y * player.gravity

        for tile in self.tiles.sprites():
            # checks if the player is collide with                                  # did we have a collision?
            # one of the tile's rectangle
            if tile.rect.colliderect(player.rect):                                  # if so, where (top or bottom)?
                if player.direction.y > 0:  # player is moving to the bottom
                    player.rect.bottom = tile.rect.top
                    player.direction.y = 0  # this line cancel gravity where the player is standing on top of a tile
                    return

                if player.direction.y < 0:  # player is moving to the top
                    player.rect.top = tile.rect.bottom
                    player.direction.y = 0
                    return

    def run(self):
        screen = self.display_surface

        # level tiles
        self.tiles.update(self.world_shift)
        self.tiles.draw(screen)
        self.scroll_x()

        # player
        self.player.update()
        self.hor_movemenet_collision()
        self.ver_movement_collision()
        self.player.draw(screen)



