from assets.entity import Entity


class Enemy(Entity):
    def __init__(self, name, img, width, height, angle, hp, coords):
        super().__init__(name, img, width, height, angle)

        self.hp = hp
        self.coords = coords
        self.x_coord = coords[0]
        self.y_coord = coords[1]
        self.sprite_path = []

    # def path(Path):
    #     """
    #     do this.
    #     """
    #     return 0
    def update(self):
        self.rect.move_ip(self.sprite_path[0][0], self.sprite_path[0,1])
        if self.rect.top < self.height:
            self.kill()
