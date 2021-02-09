"""
settings of the game
"""
import math


# global windows
WIDTH = 1200
HEIGHT = 800
FPS = 120

# game constants
TILE = 100
COLORS = {
    'white':  (255, 255, 255),
    'black':  (0, 0, 0),
    'red':    (200, 0, 0),
    'green':  (0, 200, 0),
    'blue':   (0, 0, 200),
    'gray':   (150, 150, 150),
    'purple': (120, 0, 120)
}

# ray cast
FOV = math.pi / 3
NUM_RAYS = 60
MAX_DEPTH = 1000
DELTA_ANGLE = FOV / NUM_RAYS  # This is the angle between rays
