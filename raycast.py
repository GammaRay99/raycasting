"""
This module is only for casting rays.
Contains:
    -casting ray method
"""

import math

# LOCAL IMPORTS
import game_settings
import map_world
import classes


def cast_rays(player_cords: tuple, player_angle: float) -> list:
    """
    Cast the rays of the scene
    :param player_cords: coordinates of the start of the ray
    :param player_angle: the angle the player is looking at
    :return: the list of all the rays present on the scene
    """
    rays = []
    TILE = game_settings.TILE  # shortcut
    current_angle = player_angle - (game_settings.FOV / 2)  # this var will increment from the start of the FOV
                                                            # based on the player angle to the end of it.
    for ray in range(game_settings.NUM_RAYS):
        x_ray = 0
        y_ray = 0
        for distance in range(game_settings.MAX_LENGTH):
            # we're slowly adding length to the x, y of the ray until we intersect with a wall
            # x + distance * cos(angle) determine the next x pos where we will be after moving
            # [distance] with an angle of [angle], same applies for the y formula
            x_ray = player_cords[0] + distance * math.cos(current_angle)
            y_ray = player_cords[1] + distance * math.sin(current_angle)

            if map_world.map_array[int(y_ray / TILE)][int(x_ray / TILE)]:
                # if the current x&y are on a wall, we stop
                # incrementing the distance of the ray
                break

        rays.append(classes.Ray(player_cords, (x_ray, y_ray), distance))  # finally creating the ray
        current_angle += game_settings.DELTA_ANGLE  # incrementing the angle for the next rays

    return rays
