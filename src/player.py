import pygame
from support import import_folder

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

        # player animations variables
        self.sprite_name = 'character'
        self.animations = {'idle': [],
                           'run': [],
                           'jump': [],
                           'fall': []}
        self.import_character_assets()
        [self.apply_transformation_scale(key) for key in self.animations.keys()] # resize images if needed
        self.frame_index = 0
        self.current_index = 0
        self.animation_speed = 0.15
        self.image = self.animations['idle'][self.current_index]

    def import_character_assets(self):
        character_path = f'../graphics/{self.sprite_name}'

        for animation in self.animations.keys():
            full_path = f'{character_path}/{animation}'  # complete path for a specific animation folder
            self.animations[animation] = import_folder(full_path)

        print(self.animations)

    def apply_transformation_scale(self, key='idle', size=64):
        for i, image in enumerate(self.animations[key]):
            self.animations[key][i] = pygame.transform.scale(image, (size,size)).convert_alpha()

    def animate(self):
        animation = self.animations['run']
        # loop over frame index

        self.frame_index += self.animation_speed
        if self.frame_index > len(animation):
            self.frame_index = 0
            self.current_index = 0

        self.image = animation[int(self.frame_index)]





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
        self.animate()
