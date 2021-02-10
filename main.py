import pygame

# LOCAL IMPORTS
import game_settings
import map_world
import raycast
import classes


# dimension choice
# TODO: add graphics menu selection
while True:
    dimension = input("1: 2D\n2: 3D\n")
    if dimension not in ['1', '2']:
        print("Please select a valid dimension")
        continue
    break

# pygame setup
pygame.init()
window = pygame.display.set_mode((game_settings.WIDTH, game_settings.HEIGHT))
clock = pygame.time.Clock()

# game setup
player = classes.Player((game_settings.WIDTH // 2, game_settings.HEIGHT // 2), 4, 0.04)
walls = map_world.walls
floor = classes.Floor(game_settings.COLORS['orange'])
rays = []

# main loop
game = True
while game:
    # events
    player.movement(map_world.map_array)
    rays = raycast.cast_rays((player.x, player.y), player.angle)  # creating all the Rays

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False

    # draws
    window.fill(game_settings.COLORS['bg'])

    if dimension == "1":
        # 2D
        for wall in walls:
            wall.draw_2d(window)

        for ray in rays:
            ray.draw_2d(window)

        player.draw_2d(window)

    else:
        # 3D
        floor.draw_3d(window)

        for i in range(len(rays)):
            """
            We extract from i the position x of the ray[i] 
            by multiplying i by the size of the ray, so we dont draw
            rays on each other.
            """
            rays[i].draw_3d(window, i * game_settings.RAY_WIDTH)



    # end loop
    pygame.display.flip()
    clock.tick(game_settings.FPS)
