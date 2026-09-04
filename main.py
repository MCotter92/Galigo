import pygame

from logging_config import setup_logging, get_logger
from assets.bullet import Bullet
from assets.colors import GREEN
from assets.groups import all_sprites_group, bullets_group, enemies_group
from assets.player import Player
from factory.factory import level_generator
from collisions.collisions import (
    detect_bullet_enemies_collisions,
    detect_player_enemies_collisions,
)
from renderers.renderers import draw_window

logger = get_logger("main")

WINDOW_WIDTH, WINDOW_HEIGHT = (1080, 700)
WINDOW = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
PLAYER_WIDTH, PLAYER_HEIGHT = (54, 54)
FPS = 60
VELO = 10
BULLETS_VELOCITY = 10
RED = (255, 0, 0)
HIT_COOLDOWN = 1000  # milliseconds

Player1 = Player(
    name="Player1",
    sr_entry="tinyShip3.png",
    width=27,
    height=27,
    angle=0,
    max_health=100,
    current_health=100,
    coords=((WINDOW_WIDTH / 2) - 27.3, 600),
)

all_sprites_group.add(Player1)


def main():
    logger.info("======================= Game started =============================")
    clock = pygame.time.Clock()
    run = True
    enemy_count = 3
    level_count = 1
    # NOTE: some of these sheets aren't would require a refactor in how i parse out the images due to multiple columns.
    enemy_list = ["tinyShip1.png", "tinyShip4.png", "tinyShip6.png"]
    level = level_generator(
        name=f"Level {level_count}",
        sr_entry="background-black.png",
        window_width=WINDOW_WIDTH,
        window_height=WINDOW_HEIGHT,
        num_enemies=level_count,
        enemy_list=enemy_list,
        player=Player1,
    )
    logger.info("Initial level loaded: %s", level.name)
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                logger.info("Quit event received")
                run = False
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    logger.info("Q pressed — quitting")
                    run = False
                    pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RSHIFT:
                    bullet = Bullet(
                        GREEN,
                        (
                            level.player.x_coord + (level.player.width / 2),
                            level.player.y_coord + (level.player.height / 2),
                        ),
                    )
                    bullets_group.add(bullet)
                    all_sprites_group.add(bullet)
                    logger.debug(
                        "Bullet fired at (%.0f, %.0f)",
                        bullet.rect.centerx,
                        bullet.rect.centery,
                    )
        keys_pressed = pygame.key.get_pressed()

        Player1.calculate_movement(keys_pressed, VELO, WINDOW_WIDTH, WINDOW_HEIGHT)
        detect_bullet_enemies_collisions(bullets_group, enemies_group)
        run = detect_player_enemies_collisions(Player1, enemies_group, HIT_COOLDOWN)
        bullets_group.update(WINDOW_WIDTH, WINDOW_HEIGHT)
        enemies_group.update(WINDOW_HEIGHT)
        Player1.update()
        draw_window(level, enemies_group, bullets_group, WINDOW)
        if len(level.enemies) == 0:
            level_count += 1
            enemy_count += 1
            logger.info("Level complete — advancing to level %d", level_count)
            level = level_generator(
                name=f"Level {level_count}",
                sr_entry="background-black.png",
                window_width=WINDOW_WIDTH,
                window_height=WINDOW_HEIGHT,
                num_enemies=level_count,
                enemy_list=enemy_list,
                player=Player1,
            )
            logger.info("Loaded %s with %d enemies", level.name, level_count)


if __name__ == "__main__":
    setup_logging()
    main()
