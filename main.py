import scene


game_scene = scene.Scene()

while True:
    game_scene.event_gestion()

    game_scene.render_scene()
    game_scene.render_fps()
    game_scene.render_clear()
