import pygame

from assets.healthbar import HealthBar
from assets.paths import StraightPath
from utils.utils import load_png
from assets.spritesheet_registry import SPRITESHEET_REGISTRY as sr
from utils.utils import extract_frames


class Enemy(pygame.sprite.Sprite):
    def __init__(
        self,
        name,
        spritesheet_path,
        width,
        height,
        angle,
        max_health,
        current_health,
        coords,
        speed,
        start_x,
        start_y=0,
        path=None,
    ):
        pygame.sprite.Sprite.__init__(self)
        self.name = name
        self.surf, self.rect = load_png(
            spritesheet_path,
            sr["tinyShip2.png"]["width"],
            sr["tinyShip2.png"]["height"],
            angle,
        )

        # spritesheet data
        sheet_key = spritesheet_path.split("/")[-1]
        sheet = sr[sheet_key]
        self.frames = extract_frames(
            self.surf, sheet["cols"], sheet["rows"], width, height
        )
        self.current_frame = 0
        self.surf = self.frames[0]
        self.rect = self.surf.get_rect(topleft=coords)

        # position data
        self.angel = angle
        self.width = width
        self.height = height
        self.coords = coords
        self.x_coord = coords[0]
        self.y_coord = coords[1]
        self.x_intercept = start_x
        self.start_x = start_x
        self.start_y = start_y
        self.coords[0] = self.start_x
        self.coords[1] = self.start_y
        self.speed = speed
        self.sprite_path = path or StraightPath()

        # health data
        self.max_health = max_health
        self.current_health = current_health
        self.healthbar = HealthBar(
            max_health=self.max_health,
            current_health=self.current_health,
            coords=[self.rect.topleft[0], self.rect.topleft[1]],
            width=self.width,
        )
        self.last_hit_time = 0

    def update(self, window_height):
        self.coords[0] = self.sprite_path.path(self.x_intercept, self.coords[1])
        self.coords[1] += self.speed
        self.rect.topleft = (self.coords[0], self.coords[1])
        self.healthbar.rect.bottomleft = (
            self.coords[0],
            self.coords[1] - 10,
        )

        if self.coords[1] > window_height + 25:
            self.kill()

    def draw(self, surface):
        surface.blit(self.surf, (self.coords[0], self.coords[1]))

        self.healthbar.draw(surface)
