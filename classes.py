"""
Class file of the script.
Contains:
    -player class
    -wall class
"""

import pygame
import math

# LOCAL IMPORTS
import game_settings


class Player:
    """
    This class creates the player of the world.
    Will only be drawn in 2d.
    """
    def __init__(self, cord: tuple, speed: int, turn_speed: float, color=game_settings.COLORS['purple']):
        """
        Create a player
        :param cord: current x and y of the player
        :param speed: current speed of the player
        """
        self.x = cord[0]
        self.y = cord[1]
        self.speed = speed
        self.turn_speed = turn_speed
        self.color = color
        self.angle = 0

    def movement(self, walls: list):
        """
        Movement gestion of the player
        :param walls: The walls of the map, to avoid them
        """
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:  # Angle of vue
            self.angle -= self.turn_speed
        if keys[pygame.K_RIGHT]:
            self.angle += self.turn_speed

        if keys[pygame.K_w]:
            next_x = self.x + round(self.speed * math.cos(self.angle))  # same formula then in raycast.ray_casting
            next_y = self.y + round(self.speed * math.sin(self.angle))
            if walls[int(next_y / game_settings.TILE)][int(next_x / game_settings.TILE)]:
                # if we're going into a wall,
                # we dont go into the wall.
                return

            self.x = next_x
            self.y = next_y

        if keys[pygame.K_s]:
            next_x = self.x - round(self.speed * math.cos(self.angle))
            next_y = self.y - round(self.speed * math.sin(self.angle))
            if walls[int(next_y / game_settings.TILE)][int(next_x / game_settings.TILE)]:
                return

            self.x = next_x
            self.y = next_y

        if keys[pygame.K_a]:
            next_x = self.x + round(self.speed * math.sin(self.angle))
            next_y = self.y - round(self.speed * math.cos(self.angle))
            if walls[int(next_y / game_settings.TILE)][int(next_x / game_settings.TILE)]:
                return

            self.x = next_x
            self.y = next_y

        if keys[pygame.K_d]:
            next_x = self.x - round(self.speed * math.sin(self.angle))
            next_y = self.y + round(self.speed * math.cos(self.angle))
            if walls[int(next_y / game_settings.TILE)][int(next_x / game_settings.TILE)]:
                return

            self.x = next_x
            self.y = next_y

    def draw_2d(self, win):
        pygame.draw.circle(win, self.color, [self.x, self.y], 12)
        pygame.draw.line(win, self.color, [self.x, self.y],
                         (self.x + game_settings.WIDTH * math.cos(self.angle),
                          self.y + game_settings.WIDTH * math.sin(self.angle)))  # this only to draw where
                                                                                 # he's looking at


class Wall:
    """
    This class creates the walls of the world.
    Will only be drawn in 2d.
    """
    def __init__(self, cord: tuple):
        self.x = cord[0]
        self.y = cord[1]
        self.color = game_settings.COLORS['gray']
        self.size = game_settings.TILE

    def draw_2d(self, win):
        pygame.draw.rect(win, self.color, (self.x, self.y, self.size, self.size), 2)


class Floor:
    """
    This class create the floor of the game.
    Will only be drawn in 3D.
    """
    def __init__(self, color):
        self.color = color
        self.x = 0
        self.y = game_settings.HEIGHT / 2
        self.width = game_settings.WIDTH
        self.height = game_settings.HEIGHT / 2

    def draw_3d(self, win):
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height))


class Ray:
    """
    This class represents the array of the world.
    Those will have different graphics representation
    depending of the dimension.
    """
    def __init__(self, cords_start: tuple, cords_end: tuple, length: int):
        self.start = cords_start
        self.end = cords_end
        self.length = length
        self.color = game_settings.COLORS['gray']

    def draw_2d(self, win):
        pygame.draw.line(win, self.color, self.start, self.end, 2)

    def draw_3d(self, win, x):
        """
        Draw the rays vertically, with a height depending on their length.
        If the ray have a big length, that means that the wall is far away;
        in 3D, this wall will be drawn with a small height.
        :param win: pygame surface
        :param x: the coordonate x of the ray
        """
        c = 200 / (1 + self.length * self.length * 0.00001)  # cool trick to make the color darker in the distance
        color = (c, c, c)

        height = game_settings.TILE / (self.length / 600)  # The original formula of this was:
                                                           # visible_height = true_height / distance
                                                           # since we're not in meters but in pixel, 600 is an arbitrary
                                                           # number in order to make the formula working.
        y = game_settings.HEIGHT / 2 - height / 2
        pygame.draw.rect(win, color, (x, y, game_settings.RAY_WIDTH, height))

