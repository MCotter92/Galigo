import pygame

from asset_classes.enemy import Enemy
from asset_classes.entity import Entity


def test_enemy_init():
    """Tests that the Enemy class initializes correctly."""
    WIDTH, HEIGHT = (1080, 700)
    WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
    enemy = Enemy("Goblin", "spaceship_yellow.png", 32, 32, 0, 10, (100, 100))

    assert enemy.name == "Goblin"
    assert type(enemy.img) == pygame.surface.Surface
    assert type(enemy.area) == pygame.Rect
    assert enemy.hp == 10
    assert enemy.coords == (100, 100)
    assert enemy.x_coord == 100
    assert enemy.y_coord == 100


def test_enemy_inheritance():
    """Tests that the Enemy class inherits from the Entity class."""
    WIDTH, HEIGHT = (1080, 700)
    WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
    enemy = Enemy("Goblin", "spaceship_yellow.png", 32, 32, 0, 10, (100, 100))

    assert isinstance(enemy, Enemy)
    assert isinstance(enemy, Entity)
