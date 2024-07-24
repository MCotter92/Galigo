from pygame.sprite import Group
from assets.entity import Entity
from assets.player import Player


class Level(Entity):
    def __init__(
        self,
        name,
        img,
        width,
        height,
        angle,
        enemies: Group,
        player: Player,
    ):
        super(Level, self).__init__(name, img, width, height, angle)
        self.player = player
        self.enemies = enemies
