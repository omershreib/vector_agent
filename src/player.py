import pygame


class Player(pygame.sprite.Sprite):
    def __init__(self, position):
        super().__init__()

        # general setups
        self.image = pygame.Surface((32, 64))
        self.image.fill('red')
        self.rect = self.image.get_rect(topleft=position)

        # player movement
        self.direction = pygame.math.Vector2(0, 0)
        self.velocity = 4
        self.gravity = 0.8
        self.jump_velocity = -16

    def get_input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_RIGHT]:  # player's direction to the right
            self.direction.x = 1
            return

        if keys[pygame.K_LEFT]:  # player's direction to the left
            self.direction.x = -1
            return

        if keys[pygame.K_SPACE]:  # player is jumping
            self.jump()
            return

        self.direction.x = 0  # player is not moving

    def apply_gravity(self):
        self.direction.y += self.gravity
        self.rect.y += self.direction.y

    def jump(self):
        self.direction.y = self.jump_velocity

    def update(self):
        self.get_input()

