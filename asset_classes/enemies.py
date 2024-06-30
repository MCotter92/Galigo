from asset_classes.enemy import Enemy


class Enemies:
    def __init__(self, enemies: list, positions, paths):
        self.enemies = enemies
        self.positions = positions
        self.paths = paths

    def add_enemies(self, Enemy: Enemy):
        self.enemies.append(Enemy)
