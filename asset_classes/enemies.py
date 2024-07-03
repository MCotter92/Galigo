from asset_classes.enemy import Enemy


class Enemies:
    def __init__(self, enemies: list, paths):
        self.enemies = enemies
        self.paths = paths

    def add_enemies(self, Enemy: Enemy):
        self.enemies.append(Enemy)
