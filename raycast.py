import math
import game_settings
import map_world
import classes


def ray_casting(player_cords, player_angle):
    rays = []
    TILE = game_settings.TILE  # to write faster
    current_angle = player_angle - (game_settings.FOV / 2)
    for ray in range(game_settings.NUM_RAYS):
        x_ray = 0
        y_ray = 0
        for depth in range(game_settings.MAX_DEPTH):
            x_ray = player_cords[0] + depth * math.cos(current_angle)
            y_ray = player_cords[1] + depth * math.sin(current_angle)

            if map_world.map_array[int(y_ray // TILE)][int(x_ray // TILE)]:
                break


        rays.append(classes.Ray(player_cords, (x_ray, y_ray)))
        current_angle += game_settings.DELTA_ANGLE

    return rays
