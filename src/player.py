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
        self.velocity = 2
        self.gravity = 0.8
        self.jump_velocity = -8

        # player status
        self.status = 'idle'
        self.is_faceing_right = True
        self.is_on_ground = False
        self.is_on_celling = False
        self.is_on_left = False
        self.is_on_right = False

        # player animations variables
        self.sprite_name = 'vector'
        self.animations = {'idle': [],
                           'run': [],
                           'jump': [],
                           'fall': []}
        self.import_character_assets()
        #[self.apply_transformation_scale(key) for key in self.animations.keys()] # resize images if needed
        self.frame_index = 0
        self.current_index = 0
        self.animation_speed = 0.1
        self.image = self.animations['idle'][self.current_index]

    def import_character_assets(self):
        character_path = f'../graphics/{self.sprite_name}'

        for animation in self.animations.keys():
            full_path = f'{character_path}/{animation}'  # complete path for a specific animation folder
            self.animations[animation] = import_folder(full_path)

        #print(self.animations)

    def apply_transformation_scale(self, key='idle', size=64):
        for i, image in enumerate(self.animations[key]):
            self.animations[key][i] = pygame.transform.scale(image, (size,size)).convert_alpha()

    def animate(self):
        animation = self.animations[self.status]

        # loop over frame index
        self.frame_index += self.animation_speed
        if self.frame_index > len(animation):
            self.frame_index = 0
            self.current_index = 0

        # handle image facing (left or right)
        if self.is_faceing_right:
            self.image = animation[int(self.frame_index)]

        if not(self.is_faceing_right):

            flipped_image = pygame.transform.flip(animation[int(self.frame_index)], True, False)
            self.image = flipped_image

        # rectangle setting

        # default setting
        #self.rect = self.image.get_rect(center=self.rect.center)

        if self.is_on_ground:
            self.rect = self.image.get_rect(midbottom=self.rect.midbottom)

        if not(self.is_on_ground):
            self.rect = self.image.get_rect(midtop=self.rect.midtop)

    def get_input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_RIGHT]:  # player's direction to the right
            self.direction.x = 1
            self.is_faceing_right = True
            return

        if keys[pygame.K_LEFT]:  # player's direction to the left
            self.direction.x = -1
            self.is_faceing_right = False
            return

        if keys[pygame.K_SPACE]:  # player is jumping
            self.jump()
            return

        self.direction.x = 0  # player is not moving

    def get_status(self):

        player_diraction = self.direction
        self.status = 'idle'

        # jumping
        if player_diraction.y < 0:
            self.status = 'jump'
            return

        # falling
        # if player_diraction.y > 1:
        #     self.status = 'fall'
        #     return

        # running
        if player_diraction.x:
            self.status = 'run'
            return

        # at idle status
        if not(player_diraction.x or player_diraction.y):
            self.status = 'idle'


    def apply_gravity(self):
        self.direction.y += self.gravity
        self.rect.y += self.direction.y

    def jump(self):
        self.direction.y = self.jump_velocity

    def update(self):
        self.get_input()
        self.get_status()
        self.animate()
