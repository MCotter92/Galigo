from asset_classes.enemies import Enemies
from asset_classes.entity import Entity
from asset_classes.player import Player


class Level(Entity):
    def __init__(
        self,
        name,
        img,
        width,
        height,
        angle,
        enemies: Enemies,
        player: Player,
    ):
        super().__init__(
            name,
            img,
            width,
            height,
            angle,
        )
        self.player = player
        self.enemies = enemies
