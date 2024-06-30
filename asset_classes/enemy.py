from asset_classes.entity import Entity


class Enemy(Entity):
    def __init__(self, name, img, initial_width, initial_height, initial_angle, hp):
        super().__init__(name, img, initial_width, initial_height, initial_angle)

        self.hp = hp
