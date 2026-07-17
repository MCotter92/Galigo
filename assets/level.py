from pygame.sprite import Group
from utils.utils import load_png
from assets.player import Player


class Level:
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
        self.img, self.rect = load_png(img, width, height, angle)
        self.name = name
        self.width = width
        self.height = height
        self.angle = angle
        self.player = player
        self.enemies = enemies
