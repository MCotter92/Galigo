import pygame
import os

WIDTH, HEIGHT = (500, 700)
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))

SPACESHIP_WIDTH, SPACESHIP_HEIGHT = (55, 40)
FPS = 60
VELO = 7
BULLETS_VELOCITY = 10
RED = (255, 0, 0)

SPACESHIP_IMAGE = pygame.image.load(os.path.join("Assets", "spaceship_red.png"))
SPACESHIP = pygame.transform.rotate(
    pygame.transform.scale(SPACESHIP_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 180
)

ENEMY_IMAGE = pygame.image.load(os.path.join("Assets", "spaceship_yellow.png"))
ENEMY = pygame.transform.rotate(
    pygame.transform.scale(ENEMY_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 0
)

SPACE_IMAGE = pygame.image.load(os.path.join("Assets", "space.png"))
SPACE = pygame.transform.rotate(
    pygame.transform.scale(SPACE_IMAGE, (WIDTH, HEIGHT)), 180
)

ENEMY_HIT = pygame.USEREVENT


def draw_window(spaceship, player_bullets, enemy):
    WINDOW.blit(SPACE, (0, 0))
    WINDOW.blit(SPACESHIP, (spaceship.x, spaceship.y))
    WINDOW.blit(ENEMY, (enemy.x, enemy.y))

    for bullet in player_bullets:
        pygame.draw.rect(WINDOW, RED, bullet)

    pygame.display.update()


def spaceship_movement(keys_pressed, spaceship):
    if keys_pressed[pygame.K_a] and spaceship.x - VELO > 0:  # move left
        spaceship.x -= VELO

    if (
        keys_pressed[pygame.K_d] and spaceship.x + VELO + spaceship.width < WIDTH
    ):  # move right
        spaceship.x += VELO

    if keys_pressed[pygame.K_w] and spaceship.y - VELO > 0:  # move UP
        spaceship.y -= VELO
    if (
        keys_pressed[pygame.K_s] and spaceship.y + VELO + spaceship.height < HEIGHT
    ):  # move down
        spaceship.y += VELO


def handle_bullets(player_bullets):  # add enemy as func input here when ready
    for bullet in player_bullets:
        bullet.y -= BULLETS_VELOCITY

        # if enemy.colliderect(bullet):
        #     pygame.event.post(pygame.event.Event(ENEMY_HIT))
        #     player_bullets.remove(bullet)

        # if bullet > HEIGHT:
        #     player_bullets.remove(bullet)


def main():
    spaceship = pygame.Rect(225, 600, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
    enemy = pygame.Rect(225, 600, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
    player_bullets = []
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RSHIFT:
                    bullet = pygame.Rect(
                        spaceship.x + spaceship.width // 2, spaceship.y, 5, 10
                    )

                    player_bullets.append(bullet)
        keys_pressed = pygame.key.get_pressed()

        spaceship_movement(keys_pressed, spaceship)
        handle_bullets(player_bullets)
        draw_window(spaceship, player_bullets, enemy)


main()
if __name__ == "__main__":
    main()
