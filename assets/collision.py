from assets.enemy import Enemy
from assets.player import Player


class Collision:
    def __init__(self, Enemy, Player, Bullets):
        self.Enemy = Enemy
        self.Player = Player
        self.Bullets = Bullets

    def handle_collisions(Enemy, Player, Bullets):
        """
        handles when someone get shot or run into.
        """

        # def handle_bullets(yellow_bullets, red_bullets, yellow, red):
        #     for bullet in yellow_bullets:
        #         bullet.x += BULLETS_VELOCITY
        #         if red.colliderect(bullet):  # handles red bullets
        #             pygame.event.post(pygame.event.Event(RED_HIT))
        #             yellow_bullets.remove(bullet)
        #         elif bullet.x > WIDTH:
        #             yellow_bullets.remove(bullet)

        #     for bullet in red_bullets:
        #         bullet.x -= BULLETS_VELOCITY
        #         if yellow.colliderect(bullet):  # handles yellow bullets
        #             pygame.event.post(pygame.event.Event(YELLOW_HIT))
        #             red_bullets.remove(bullet)
        #         elif bullet.x < 0:
        #             red_bullets.remove(bullet)
        #         return 0
