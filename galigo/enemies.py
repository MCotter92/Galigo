from entity import Entity
import player


class Enemies(player):
    def __init__(self, player, positions, paths):
        super().__init__()
        self.enemies = [player]
        self.positions = [positions]
        self.paths = [paths]
