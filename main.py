import pygame

from asset_classes.enemies import Enemies
from asset_classes.enemy import Enemy
from asset_classes.level import Level
from asset_classes.player import Player

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
    coords=((WIDTH / 2) - 27.3, 600),
)

# ENEMY_HIT = pygame.USEREVENT


def create_enemies(num, width, height):
    i = 0
    x = 50
    y = 200
    enemies = Enemies([], [])
    while i < num:
        ENEMY = Enemy(
            f"Enemy{i}",
            "spaceship_yellow.png",
            width,
            height,
            angle=0,
            hp=50,
            coords=(x, y),
        )
        enemies.add_enemies(ENEMY)
        i += 1
        x += 100
    return enemies


def level_generator(name, image, resolution, num_enemies) -> Level:
    return Level(
        name,
        image,
        resolution[0],
        resolution[1],
        0,
        create_enemies(num_enemies, SPACESHIP_WIDTH - 5, SPACESHIP_HEIGHT - 5),
        SPACESHIP,
    )


def draw_window(level: Level, player_bullets):
    WINDOW.blit(level.img, (0, 0))
    WINDOW.blit(level.player.img, (level.player.x_coord, level.player.y_coord))

    for enemy in level.enemies.enemies:
        WINDOW.blit(enemy.img, (enemy.x_coord, enemy.y_coord))

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
    enemy_count = 3
    level_count = 1
    level = level_generator(
        f"Level {level_count}", "space.png", (WIDTH, HEIGHT), enemy_count
    )
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
        draw_window(level, player_bullets)
        if len(level.enemies.enemies) == 0:
            level_count += 1
            enemy_count += 3
            level = level_generator(
                f"Level {level_count}", "space.png", (WIDTH, HEIGHT), enemy_count
            )


if __name__ == "__main__":
    main()
