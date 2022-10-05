from os import walk
import pygame
import imghdr

def import_folder(path):
    images_list = []
    for _, __, images in walk(path):
        for image in images:
            img_path = f'{path}/{image}'
            assert imghdr.what(img_path), f'Unrecognized image format. Do {img_path} is an image at all?'
            sprite_image = pygame.image.load(img_path).convert_alpha()
            images_list.append(sprite_image)

    return images_list
