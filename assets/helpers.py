import math

# import pygame

# from assets.entity import Entity
# from assets.enemy import Enemy
# from assets.player import Player


def straight_line(x, height):
    line_path = []
    for i in range(0, height):
        y = i

        line_path.append((x, y))
    return line_path

    # def sine():
    #     pass

    # def cosine(start, end, wave_length, amplitude):

    #     return 0

    # def cosh(start, end, wave_length, amplitude):

    #     return 0

    # def sinh(start, end, wave_length, amplitude):

    #     return 0
