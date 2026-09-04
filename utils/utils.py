import pygame

from logging_config import get_logger
from assets.spritesheet_registry import SPRITESHEET_REGISTRY as SR

logger = get_logger("utils")


def load_png(sr_entry, width, height, angle_x=0):
    """Load image and return image object"""

    try:
        surf = pygame.image.load(SR[sr_entry]["path"])
        if surf.get_alpha() is None:
            surf = surf.convert()
        else:
            surf = surf.convert_alpha()
        scale = pygame.transform.scale(surf, (width, height))
        surf = pygame.transform.rotate(scale, angle_x)
        logger.debug("Loaded asset: %s", sr_entry)
    except FileNotFoundError as e:
        logger.error("Cannot load image: %s", sr_entry)
        raise e
    return surf, surf.get_rect()


def extract_frames(sheet, cols, rows, target_w, target_h):
    frame_width = sheet.get_width() // cols
    frame_height = sheet.get_height() // rows
    frames = []
    for row in range(rows):
        for col in range(cols):
            frame = sheet.subsurface(
                col * frame_width, row * frame_height, frame_width, frame_height
            )
            frame = pygame.transform.scale(frame, (target_w, target_h))
            frames.append(frame)
    return frames
