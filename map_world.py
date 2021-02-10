"""
This module handles the map gestion of the scene.
Contains:
    -the map
    -all the walls-objects
    -all the walls positions
"""

# LOCAL IMPORTS
import classes
import game_settings

map_array = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1],
    [1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1],
    [1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1],
    [1, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]

walls = []
walls_cord = []

for y, row in enumerate(map_array):
    for x, tile in enumerate(row):
        """
        We're iterating in the matrix and extracting x&y of each wall
        """
        if tile:
            walls_cord.append((x, y))
            walls.append(classes.Wall((x * game_settings.TILE, y * game_settings.TILE)))
