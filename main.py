import pygame

import game_settings
import map_world
import raycast
import classes

dimension = int(input("1: 2D\n2: 3D\n"))

# pygame setup
pygame.init()
window = pygame.display.set_mode((game_settings.WIDTH, game_settings.HEIGHT))
clock = pygame.time.Clock()

# game setup
player = classes.Player((game_settings.WIDTH // 2, game_settings.HEIGHT // 2), 4, 0.04)
walls = map_world.walls
rays = []

# main loop
game = True
while game:
    # events
    player.movement()
    rays = raycast.ray_casting((player.x, player.y), player.angle)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False

    # draws
    window.fill(game_settings.COLORS['black'])
    for wall in map_world.walls:
        wall.draw(window)

    for ray in rays:
        ray.draw(window)

    player.draw(window, game_settings.COLORS['purple'])

        
    # end loop
    pygame.display.flip()
    clock.tick(game_settings.FPS)

