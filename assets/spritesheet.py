import pygame
from assets.entity import Entity


class SpriteSheet(Entity):
    def __init__(self, spritesheet_path):
        super().__init__(img=spritesheet_path)

        return image
