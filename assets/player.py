import pygame

from assets.entity import Entity


class Player(Entity):
    def __init__(self, name, img, width, height, angle, hp, coords):
        super().__init__(name, img, width, height, angle)
        self.width = width
        self.height = height
        self.hp = hp
        self.coords = coords
        self.x_coord = coords[0]
        self.y_coord = coords[1]
        self.numlives = 3

    def register_death(self):
        self.numlives = self.numlives - 1
        if self.numlives == 0:
            self.kill()
            pygame.quit()

    def increase_life_count(self):
        self.numlives += 1
