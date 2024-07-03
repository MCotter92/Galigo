import pygame
import pytest

from asset_classes.entity import Entity
from utils.utils import load_png


@pytest.fixture
def entity():
    """Fixture to create an Entity instance for testing."""
    name = "TestEntity"
    img = "space.png"
    initial_width = 1080
    initial_height = 700
    initial_angle = 0
    return Entity(name, img, initial_width, initial_height, initial_angle)


def test_entity_init(entity):
    """Tests that the Entity class initializes correctly."""
    assert entity.name == "TestEntity"
    assert entity.img is not None
    assert entity.rect is not None
    assert entity.screen is not None
    assert entity.area is not None


def test_entity_screen_and_area(entity):
    """Tests that the screen and area attributes are set correctly."""
    assert entity.screen == pygame.display.get_surface()
    assert entity.area == entity.screen.get_rect()
