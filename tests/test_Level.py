import pygame
import pytest

from asset_classes.enemies import Enemies
from asset_classes.enemy import Enemy
from asset_classes.entity import Entity
from asset_classes.level import Level
from asset_classes.player import Player


@pytest.fixture
def level():
    """Fixture to create a Level instance for testing."""
    enemies = Enemies(
        [Enemy("Goblin", "spaceship_yellow.png", 32, 32, 0, 10, (100, 100))], []
    )
    player = Player("Player", "spaceship_red.png", 32, 32, 0, 100, (200, 200))
    return Level("TestLevel", "space.png", 800, 600, 0, enemies, player)


def test_level_init(level):
    """Tests that the Level class initializes correctly."""
    assert level.name == "TestLevel"
    assert type(level.img) == pygame.surface.Surface
    assert level.enemies == level.enemies
    assert level.player == level.player


def test_level_inheritance(level):
    """Tests that the Level class inherits from the Entity class."""
    assert isinstance(level, Level)
    assert isinstance(level, Entity)
