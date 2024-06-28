from entity import Entity
from pygame import transform


class Player(Entity):
    def __init__(self, name, img, width, height, hp):
        super().__init__(name, img)
        self.width = width
        self.height = height
        self.hp = hp
        self.name = name
        self.img = img

        self.rotate(180)

    
