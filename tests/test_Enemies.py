import pygame

from asset_classes.enemies import Enemies
from asset_classes.enemy import Enemy


def test_enemies_init():
    """Tests that the Enemies class initializes correctly."""
    WIDTH, HEIGHT = (1080, 700)
    WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
    enemies = [Enemy("Goblin", "spaceship_yellow.png", 32, 32, 0, 10, (100, 100))]
    paths = ["path1", "path2"]
    enemies_group = Enemies(enemies, paths)

    assert enemies_group.enemies == enemies
    assert enemies_group.paths == paths


def test_enemies_add_enemies():
    """Tests that the add_enemies method adds a new Enemy to the list."""
    WIDTH, HEIGHT = (1080, 700)
    WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
    enemies = [Enemy("Goblin", "spaceship_yellow.png", 32, 32, 0, 10, (100, 100))]
    paths = ["path1", "path2"]
    enemies_group = Enemies(enemies, paths)

    new_enemy = Enemy("Orc", "spaceship_yellow.png", 32, 32, 0, 15, (200, 200))
    enemies_group.add_enemies(new_enemy)

    assert len(enemies_group.enemies) == 2
    assert enemies_group.enemies[1] == new_enemy
