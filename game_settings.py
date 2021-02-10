"""
All the constants of the game
Contains:
    -window constants
    -game constants
    -ray constants
"""
import pygame
import math


# global window constants
WIDTH = 1200
HEIGHT = 800
FPS = 60


# ray cast constants
FOV = math.pi / 3  # we're working with trigonometric values
NUM_RAYS = 80
MAX_LENGTH = 800  # The maximal length of the rays
DELTA_ANGLE = FOV / NUM_RAYS  # This is the angle between rays
RAY_WIDTH = WIDTH // NUM_RAYS


# game constants
BUTTON_SIZE = (500, 400)
TILE = 100
BG_COLOR = 200 / (1 + MAX_LENGTH * MAX_LENGTH * 0.00001)  # this represent the color of the sky, but also the color
                                                          # of the rays that are far away, it creates a fog effect.
FONT = lambda size: pygame.font.SysFont('verdana', size, True)
COLORS = {
    'white':  (200, 200, 200),
    'black':  (50, 50, 50),
    'orange': (150, 80, 40),
    'green':  (0, 200, 0),
    'blue':   (0, 0, 200),
    'gray':   (150, 150, 150),
    'purple': (120, 0, 120),
    'red':    (200, 0, 0),
    'bg':     (BG_COLOR, BG_COLOR, BG_COLOR)
}
