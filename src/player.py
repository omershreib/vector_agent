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
        is_player_moves = bool(bool(keys[pygame.K_RIGHT] or bool(keys[pygame.K_LEFT])))

        if keys[pygame.K_RIGHT]:
            self.direction.x = 1

        elif keys[pygame.K_LEFT]:
            self.direction.x = -1

        else:
            self.direction.x = 0
        #print(self.direction.x)


    def update(self):
        self.get_input()
        self.rect.x += self.direction.x * self.velocity
