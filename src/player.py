import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, position):
        super().__init__()

        # general setups
        self.image = pygame.Surface((32,64))
        self.image.fill('red')
        self.rect = self.image.get_rect(topleft=position)
        self.direction = pygame.math.Vector2(0,0)

        # player default attributes
        self.is_looking_left = False

        # player attributes
        self.velocity = 4

    def get_input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_RIGHT]:    # player's direction to the right
            self.direction.x = 1
            return

        if keys[pygame.K_LEFT]:     # player's direction to the left
            self.direction.x = -1
            return

        self.direction.x = 0    # player is not moving



    def update(self):
        self.get_input()
        self.rect.x += self.direction.x * self.velocity
