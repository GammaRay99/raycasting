"""
Class file of the script.
Contains:
    -player class
    -wall class
"""
import pygame
import math

import game_settings


class Player:
    def __init__(self, pos, speed, turn_speed):
        """
        Create a player
        :param pos: current x and y of the player
        :param speed: current speed of the player
        """
        self.speed = speed
        self.turn_speed = turn_speed
        self.x = pos[0]
        self.y = pos[1]
        self.angle = 0

    def movement(self):
        """
        Movement gestion of the player
        """
        keys = pygame.key.get_pressed()

        if keys[pygame.K_w]:
            self.x += round(self.speed * math.cos(self.angle))
            self.y += round(self.speed * math.sin(self.angle))
        if keys[pygame.K_s]:
            self.x -= round(self.speed * math.cos(self.angle))
            self.y -= round(self.speed * math.sin(self.angle))
        if keys[pygame.K_a]:
            self.x += round(self.speed * math.sin(self.angle))
            self.y -= round(self.speed * math.cos(self.angle))
        if keys[pygame.K_d]:
            self.x -= round(self.speed * math.sin(self.angle))
            self.y += round(self.speed * math.cos(self.angle))

        if keys[pygame.K_LEFT]:
            self.angle -= self.turn_speed
        if keys[pygame.K_RIGHT]:
            self.angle += self.turn_speed

    def draw(self, win, color):
        pygame.draw.circle(win, color, [self.x, self.y], 12)
        pygame.draw.line(win, color, [self.x, self.y],
                         (self.x + game_settings.WIDTH * math.cos(self.angle),
                          self.y + game_settings.WIDTH * math.sin(self.angle)))


class Wall:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.color = game_settings.COLORS['gray']
        self.size = game_settings.TILE

    def draw(self, win):
        pygame.draw.rect(win, self.color, (self.x, self.y, self.size, self.size), 2)



class Ray:
    def __init__(self, cords_start, cords_end):
        self.start = cords_start
        self.end = cords_end
        self.color = game_settings.COLORS['gray']

    def draw(self, win):
        pygame.draw.line(win, self.color, self.start, self.end, 2)
