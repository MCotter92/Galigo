from entity import Entity
from asset_classes.enemy import Enemies


class Level(Entity):
    def __init__(self, powerUP, enemiesNumUp):
        super().__init__()
        self.powerUP = powerUP
        self.numUP = enemiesNumUp

    def increaseLevel():
        "do stuff"
