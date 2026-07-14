from assets.enemy import Enemy
from assets.level import Level
from assets.paths import ReverseZigZagPath, StraightPath
from assets.groups import enemies, all_sprites
from assets.spritesheet_registry import SPRITESHEET_REGISTRY as sr


def create_enemies(num, spaceship_name):
    i = 0
    x = 50
    y = 200
    if num > 10:
        num = 10

    while i < num:
        enemy = Enemy(
            name=f"Enemy{i}",
            spritesheet_path=sr[spaceship_name]["path"],
            width=36,
            height=35,
            angle=0,
            max_health=100,
            current_health=100,
            coords=[x, y],
            start_x=x,
            speed=1,
            path=StraightPath(),
        )
        enemies.add(enemy)
        all_sprites.add(enemy)
        i += 1
        x += 100
    return enemies


def level_generator(
    name,
    image,
    window_width,
    window_height,
    num_enemies,
    enemy_name,
    player,
) -> Level:
    return Level(
        name=name,
        img=image,
        width=window_width,
        height=window_height,
        angle=0,
        enemies=create_enemies(num_enemies, enemy_name),
        player=player,
    )
