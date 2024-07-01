import os

import pygame
import pytest

from utils.utils import load_png


@pytest.fixture
def mock_pygame_image_load(monkeypatch):
    """Mock pygame.image.load to return a test image."""
    mock_image = pygame.Surface((32, 32))
    monkeypatch.setattr(pygame.image, "load", lambda _: mock_image)


def test_load_png_success(mock_pygame_image_load):
    """Tests that load_png returns an image and rect when successful."""
    name = "test_image.png"
    width = 64
    height = 32
    angle_x = 45

    image, rect = load_png(name, width, height, angle_x)

    assert image is not None
    assert rect is not None
    assert image.get_width() == width + 3
    assert image.get_height() == height * 2 + 3
    assert rect.width == width + 3
    assert rect.height == height * 2 + 3


def test_load_png_file_not_found(monkeypatch):
    """Tests that load_png raises SystemExit when the file is not found."""
    monkeypatch.setattr(os.path, "join", lambda *args: "nonexistent_file.png")
    with pytest.raises(SystemExit):
        load_png("test_image.png", 32, 32)


def test_load_png_alpha(mock_pygame_image_load, monkeypatch):
    """Tests that load_png handles images with and without alpha channels correctly."""
    # Mock image with alpha channel
    mock_image = pygame.Surface((32, 32), pygame.SRCALPHA)
    monkeypatch.setattr(pygame.image, "load", lambda _: mock_image)
    image, rect = load_png("test_image.png", 32, 32)
    assert image.get_alpha() is not None

    # Mock image without alpha channel
    mock_image = pygame.Surface((32, 32))
    monkeypatch.setattr(pygame.image, "load", lambda _: mock_image)
    image, rect = load_png("test_image.png", 32, 32)
    assert image.get_alpha() is None
