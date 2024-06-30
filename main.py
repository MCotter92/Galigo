import os

import pygame

from asset_classes.enemies import Enemies
from asset_classes.enemy import Enemy
from asset_classes.player import Player
from utils.utils import load_png

WIDTH, HEIGHT = (1080, 700)
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))

SPACESHIP_WIDTH, SPACESHIP_HEIGHT = (55, 40)
FPS = 60
VELO = 7
BULLETS_VELOCITY = 10
RED = (255, 0, 0)

SPACESHIP = Player(
    name="Player1",
    img="spaceship_red.png",
    width=SPACESHIP_WIDTH,
    height=SPACESHIP_HEIGHT,
    angle=180,
    hp=100,
    x_coord=225,
    y_coord=600,
)

SPACE = load_png("space.png", WIDTH, HEIGHT, 0)

# ENEMY_HIT = pygame.USEREVENT


def create_enemies():
    i = 0
    x = 225
    y = 200
    enemies = Enemies([], [])
    while i < 5:
        ENEMY = Enemy(
            f"Enemy{i}",
            "spaceship_yellow.png",
            SPACESHIP_WIDTH - 3,
            SPACESHIP_HEIGHT - 3,
            angle=0,
            hp=50,
            coord=(x, y),
        )
        enemies.add_enemies(ENEMY)
        i += 1
        x += 100
    return enemies


def draw_window(player_bullets):
    WINDOW.blit(SPACE[0], (0, 0))
    WINDOW.blit(SPACESHIP.img, (SPACESHIP.x_coord, SPACESHIP.y_coord))

    enemies = create_enemies()
    for enemy in enemies.enemies:
        WINDOW.blit(enemy.img, enemy.coord)

    for bullet in player_bullets:
        pygame.draw.rect(WINDOW, RED, bullet)

    pygame.display.update()


def spaceship_movement(keys_pressed):
    # move left
    if keys_pressed[pygame.K_a] and SPACESHIP.x_coord - VELO > 0:
        SPACESHIP.x_coord = SPACESHIP.x_coord - VELO

    # move right
    if keys_pressed[pygame.K_d] and SPACESHIP.x_coord + VELO + SPACESHIP.width < WIDTH:
        SPACESHIP.x_coord = SPACESHIP.x_coord + VELO

    # move up
    if keys_pressed[pygame.K_w] and SPACESHIP.y_coord - VELO > 0:
        if SPACESHIP.y_coord <= 500:
            SPACESHIP.y_coord = 500
        else:
            SPACESHIP.y_coord = SPACESHIP.y_coord - VELO

    # move down
    if (
        keys_pressed[pygame.K_s]
        and SPACESHIP.y_coord + VELO + SPACESHIP.height < HEIGHT
    ):
        SPACESHIP.y_coord += VELO


def handle_bullets(player_bullets):  # add enemy as func input here when ready
    for bullet in player_bullets:
        bullet.y -= BULLETS_VELOCITY

        # if enemy.colliderect(bullet):
        #     pygame.event.post(pygame.event.Event(ENEMY_HIT))
        #     player_bullets.remove(bullet)

        # if bullet > HEIGHT:
        #     player_bullets.remove(bullet)


def main():
    player_bullets = []
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RSHIFT:
                    bullet = pygame.Rect(
                        SPACESHIP.x_coord + SPACESHIP.width // 2,
                        SPACESHIP.y_coord,
                        5,
                        10,
                    )

                    player_bullets.append(bullet)
        keys_pressed = pygame.key.get_pressed()

        spaceship_movement(keys_pressed)
        handle_bullets(player_bullets)
        draw_window(player_bullets)


if __name__ == "__main__":
    main()
