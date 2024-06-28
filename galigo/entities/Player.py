import os

import Entity
from pygame import image, transform


class Player(Entity):
    def __init__(self, name, image, width, height, hp):
        super().__init__(self, name, image)
        self.name = name
        self.image = image.load(os.path.join("../Assets", name))
        self.width = width
        self.height = height
        self.hp = hp

        self.rotate(180)

    def rotate(self, degree):
        self.image = transform.rotate(
            transform.scale(self.image, (self.width, self.height), degree)
        )
