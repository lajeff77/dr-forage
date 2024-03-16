import pygame
from ForestScene import ForestScene
from Item import Item
from VillageScene import VillageScene
pygame.init()

screen = pygame.display.set_mode([500, 500])
pygame.display.set_caption("Dr.Forage")
clock = pygame.time.Clock()
scene = VillageScene()
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
    scene.update(events, pressed_keys)
    scene.render(screen)

    # update scene
    scene = scene.next

    pygame.display.flip()
    clock.tick(fps)

pygame.quit()
