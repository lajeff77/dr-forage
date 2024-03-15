import pygame
from SceneManager import SceneManager
from ForestScene import ForestScene
from WorkStationScene import WorkStationScene

pygame.init()

screen = pygame.display.set_mode([500, 500])
pygame.display.set_caption("Dr.Forage")
pygame.mouse.set_visible(False)
clock = pygame.time.Clock()
scene_manager = SceneManager()
scene_manager.add_scene('forest', ForestScene(scene_manager))
scene_manager.add_scene('workstation', WorkStationScene(scene_manager))
scene_manager.switch_to_scene('workstation')
fps = 60
running = True

while running:

    # process events
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            running = False

    # get key inputs
    pressed_keys = pygame.key.get_pressed()

    # update
    scene_manager.get_current_scene().update(events, pressed_keys)

    # render
    scene_manager.get_current_scene().render(screen)

    pygame.display.flip()
    clock.tick(fps)

pygame.quit()
