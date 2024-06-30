import pygame

from asset_classes.entity import Entity


class Player(Entity):
    def __init__(self, name, img, width, height, angle, hp, x_coord, y_coord):
        super().__init__(name, img, width, height, angle)
        self.width = width
        self.height = height
        self.hp = hp
        self.x_coord = x_coord
        self.y_coord = y_coord
        self.numlives = 3

    def register_death(self):
        self.numlives = self.numlives - 1
        if self.numlives == 0:
            pygame.quit()
            
    def increase_life_count(self):
        self.numlives += 1
