from assets.entity import Entity
from assets.path import Path


class Enemy(Entity):
    def __init__(self, name, img, width, height, angle, hp, coords):
        super().__init__(name, img, width, height, angle)

        self.hp = hp
        self.coords = coords
        self.x_coord = coords[0]
        self.y_coord = coords[1]

    def path(Path):
        """
        do this.
        """
        return 0
