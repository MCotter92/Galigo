import os

from pygame import Surface, image, transform


class Entity:
    def __init__(self, name, img):
        self.name = name
        self.img = self.get_image_surface(
            os.path.join(os.path.dirname(__file__), "..", "Assets", img)
        )

    def get_image_surface(self, image_path) -> Surface:
        return image.load(image_path)

    def rotate(self, degree):
        self.img = transform.rotate(
            transform.scale(self.img, (self.width, self.height), degree)
        )
