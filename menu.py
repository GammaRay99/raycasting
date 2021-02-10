"""
This module handles the menu of the game
"""

import pygame

# LOCAL IMPORTS
import game_settings


class Button:
    def __init__(self, cords: tuple, dimension: str):
        self.x = cords[0]
        self.y = cords[1]

        self.color = game_settings.COLORS['gray']
        self.text = game_settings.FONT(75).render(dimension, 1, game_settings.COLORS['blue'])
        self.hitbox = (self.x, self.y, game_settings.BUTTON_SIZE[0], game_settings.BUTTON_SIZE[1])

    def check_clicks(self):
        mouse_pos = pygame.mouse.get_pos()
        if pygame.Rect(self.hitbox).collidepoint(mouse_pos[0], mouse_pos[1]):
            self.color = game_settings.COLORS['black']
            if pygame.mouse.get_pressed()[0]:
                return True
        else:
            self.color = game_settings.COLORS['gray']
            return False

    def draw(self, win):
        pygame.draw.rect(win, self.color, self.hitbox)
        win.blit(self.text, (self.x + (game_settings.BUTTON_SIZE[0]/2) - 50,
                             self.y + (game_settings.BUTTON_SIZE[1]/2) - 50))


def dimension_selection_menu(win):
    button_2d_cords = (game_settings.WIDTH / 2 - (game_settings.BUTTON_SIZE[0] + 30),
                       game_settings.HEIGHT / 2 - game_settings.BUTTON_SIZE[1] / 2)
    button_3d_cords = (game_settings.WIDTH / 2 + 30,
                       game_settings.HEIGHT / 2 - game_settings.BUTTON_SIZE[1] / 2)

    button_2d = Button(button_2d_cords, "2D")
    button_3d = Button(button_3d_cords, "3D")

    choice = False
    while not choice:
        # events
        if button_2d.check_clicks():
            return "2D"

        if button_3d.check_clicks():
            return "3D"

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()

        # draws
        win.fill(game_settings.COLORS['bg'])

        button_2d.draw(win)
        button_3d.draw(win)

        pygame.display.flip()
