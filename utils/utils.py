import pygame


def load_png(img_path, width, height, angle_x=0):
    """Load image and return image object"""

    try:
        image = pygame.image.load(img_path)
        if image.get_alpha() is None:
            image = image.convert()
        else:
            image = image.convert_alpha()
        scale = pygame.transform.scale(image, (width, height))
        image = pygame.transform.rotate(scale, angle_x)
    except FileNotFoundError:
        print(f"Cannot load image: {img_path}")
        raise SystemExit
    return image, image.get_rect()


def extract_frames(sheet, cols, rows, target_w, target_h):
    frame_w = sheet.get_width() // cols
    frame_h = sheet.get_height() // rows
    frames = []
    for row in range(rows):
        for col in range(cols):
            frame = sheet.subsurface(col * frame_w, row * frame_h, frame_w, frame_h)
            frame = pygame.transform.scale(frame, (target_w, target_h))
            frames.append(frame)
    return frames
