from assets.entity import Entity


class Enemy(Entity):
    def __init__(self, name, img, width, height, angle, hp, coords):
        super().__init__(name, img, width, height, angle)

        self.hp = hp
        self.coords = coords
        self.x_coord = coords[0]
        self.y_coord = coords[1]
        self.sprite_path = []
        self.width = width
        self.height = height

    # def path(Path):
    #     """
    #     do this.
    #     """
    #     return 0
    def update(self, window_height, window_width):
        self.y_coord += 1
        self.rect.move_ip(self.x_coord, self.y_coord)
        if self.y_coord > window_height + 25:
            self.kill()
