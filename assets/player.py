import pygame

from utils.utils import load_png
from assets.healthbar import HealthBar
from assets.spritesheet_registry import SPRITESHEET_REGISTRY as sr
from utils.utils import extract_frames


class Player(pygame.sprite.Sprite):
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
    ):
        pygame.sprite.Sprite.__init__(self)
        self.name = name
        self.surf, self.rect = load_png(
            spritesheet_path,
            sr["tinyShip3.png"]["width"],
            sr["tinyShip3.png"]["height"],
            angle,
        )

        sheet_key = spritesheet_path.split("/")[-1]
        sheet = sr[sheet_key]
        self.frames = extract_frames(
            self.surf, sheet["cols"], sheet["rows"], width, height
        )
        self.current_frame = 0
        self.surf = self.frames[0]
        self.rect = self.surf.get_rect(topleft=coords)
        self.bottomleft = self.rect.bottomleft

        # position data
        self.width = width  # render width
        self.height = height  # render height
        self.coords = coords
        self.x_coord = coords[0]
        self.y_coord = coords[1]

        # health data
        self.numlives = 1
        self.max_health = max_health
        self.current_health = current_health
        self.healthbar = HealthBar(
            max_health=self.max_health,
            current_health=self.current_health,
            coords=[self.bottomleft[0], self.bottomleft[1]],
            width=self.width,
        )
        self.last_hit_time = 0

    def draw(self, surface):
        surface.blit(self.frames[self.current_frame], (self.x_coord, self.y_coord))
        self.healthbar.draw(surface)

    def calculate_movement(self, keys_pressed, velo, width, height):
        # move left
        if keys_pressed[pygame.K_a] and self.x_coord - velo > 0:
            self.x_coord = self.x_coord - velo

        # move right
        if keys_pressed[pygame.K_d] and self.x_coord + velo + self.width < width:
            self.x_coord = self.x_coord + velo

        # move up
        if keys_pressed[pygame.K_w] and self.y_coord - velo > 0:
            if self.y_coord <= 500:
                self.y_coord = 500
            else:
                self.y_coord = self.y_coord - velo

        # move down
        if keys_pressed[pygame.K_s] and self.y_coord + velo + self.height < height:
            self.y_coord += velo

    def update_pos(self):
        if self.rect is not None:
            self.rect.topleft = (self.x_coord, self.y_coord)
            self.healthbar.rect.topleft = (
                self.rect.bottomleft[0],
                self.rect.bottomleft[1] + 10,
            )

    def update(self, now):
        self.current_frame = (now // 200) % len(self.frames)
        self.update_pos()

    def register_death(self):
        run = True
        self.numlives = self.numlives - 1
        if self.numlives == 0:
            self.kill()
            run = False
            return run
        else:
            self.max_health = 100
        return run

    def increase_life_count(self):
        self.numlives += 1
