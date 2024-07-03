import pygame
import pytest

from asset_classes.player import Player


@pytest.fixture
def player():
    """Fixture to create a Player instance for testing."""
    return Player("TestPlayer", "spaceship_red.png", 32, 32, 0, 100, (200, 200))


def test_player_init(player):
    """Tests that the Player class initializes correctly."""
    assert player.name == "TestPlayer"
    assert type(player.img) == pygame.surface.Surface
    assert player.width == 32
    assert player.height == 32
    assert player.hp == 100
    assert player.coords == (200, 200)
    assert player.x_coord == 200
    assert player.y_coord == 200
    assert player.numlives == 3


def test_player_register_death(player, monkeypatch):
    """Tests that the register_death method correctly decrements lives and kills the player."""
    # Mock pygame.quit() to prevent actual program exit
    monkeypatch.setattr(pygame, "quit", lambda: None)

    # Test decrementing lives
    player.register_death()
    assert player.numlives == 2

    # Test killing the player when lives reach 0
    player.numlives = 1
    player.register_death()
    assert player.numlives == 0
    # We can't directly assert that the player is killed, as kill() is a method from Entity
    # We can add a test to check if the player is removed from a group or has a specific flag set


def test_player_increase_life_count(player):
    """Tests that the increase_life_count method correctly increments lives."""
    player.increase_life_count()
    assert player.numlives == 4
