import pygame

from asset_classes.entity import Entity


class Player(Entity):
    def __init__(self, name, img, width, height, angle, hp):
        super().__init__(name, img, width, height, angle)

        self.hp = hp
