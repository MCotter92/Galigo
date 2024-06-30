import os

import pygame


def load_png(name, width, height, angle_x=0):
    """Load image and return image object"""
    fullname = os.path.join("Assets", name)
    try:
        image = pygame.image.load(fullname)
        if image.get_alpha() is None:
            image = image.convert()
        else:
            image = image.convert_alpha()
        scale = pygame.transform.scale(image, (width, height))
        image = pygame.transform.rotate(scale, angle_x)
    except FileNotFoundError:
        print(f"Cannot load image: {fullname}")
        raise SystemExit
    return image, image.get_rect()
