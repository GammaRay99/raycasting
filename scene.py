"""
This module gather all the elements to the scene
"""
import pygame

import game_settings
import map_world
import raycast
import classes
import menu


class Scene:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode((game_settings.WIDTH, game_settings.HEIGHT))
        self.clock = pygame.time.Clock()

        self.dimension = None

        self.map_array = map_world.map_array
        self.player = classes.Player((game_settings.WIDTH // 2, game_settings.HEIGHT // 2), 4, 0.04)
        self.walls = map_world.walls
        self.walls_cords = map_world.walls_cord
        self.rays = []
        self.floor = classes.Floor(game_settings.COLORS['orange'])

    def event_gestion(self):
        """
        This function handles:
            -player movements
            -ray casting
            -close window
            -dimension choice
        """
        self.player.movement(self.map_array)
        self.rays = raycast.cast_rays((self.player.x, self.player.y), self.player.angle)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()

        if not self.dimension:
            self.dimension = menu.dimension_selection_menu(self.window)

        if pygame.key.get_pressed()[pygame.K_ESCAPE]:  # if we press escape, we can change the dimension
            self.dimension = None

    def render_2d_scene(self):
        """
        This function create the 2D scene, drawing:
            -the walls
            -the rays
            -the player
        :return:
        """
        self.window.fill(game_settings.COLORS['bg'])

        for wall in self.walls:
            wall.draw_2d(self.window)

        for ray in self.rays:
            ray.draw_2d(self.window)

        self.player.draw_2d(self.window)

    def render_3d_scene(self):
        """
        This function create the 3D scene, drawing:
            -the floor
            -the rays
        """
        self.window.fill(game_settings.COLORS['bg'])

        self.floor.draw_3d(self.window)

        for i in range(len(self.rays)):
            """
            We extract from i the position x of the ray[i] 
            by multiplying i by the size of the ray, so we dont draw
            rays on each other.
            """
            self.rays[i].draw_3d(self.window, i * game_settings.RAY_WIDTH)

    def render_scene(self):
        if self.dimension == "2D":
            self.render_2d_scene()
        else:
            self.render_3d_scene()

    def render_fps(self):
        """
        This function render the fps of the player
        Fps wil be red if < 15
        """
        current_fps = int(self.clock.get_fps())
        color = game_settings.COLORS["red" if current_fps < 15 else "green"]
        fps_text = game_settings.FONT(15).render(str(int(self.clock.get_fps())), 0, color)
        self.window.blit(fps_text, (10, 10))

    def render_clear(self):
        """
        Render end loop
        """
        pygame.display.flip()
        self.clock.tick(game_settings.FPS)
