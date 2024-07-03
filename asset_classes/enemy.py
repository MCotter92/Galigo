from asset_classes.entity import Entity
from asset_classes.path import Path


class Enemy(Entity):
    def __init__(self, name, img, width, height, angle, hp, coord):
        super().__init__(name, img, width, height, angle)

        self.hp = hp
        self.coord = coord

    def path(Path):
        """
        do this.
        """
        return 0
