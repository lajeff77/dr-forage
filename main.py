import pygame
from pygame.locals import (
     K_i
)
from ForagableItem import ForagableItem
from Player import Player

pygame.init()

screen = pygame.display.set_mode([500, 500])
pygame.display.set_caption("Dr.Forage")
tree1 = ForagableItem("resources/sprites/lemon-tree.png", "resources/sprites/tree.png", 250, 120, "lemon", 3)
tree2 = ForagableItem("resources/sprites/honey-tree.png", "resources/sprites/tree.png", 50, 150, "honey", 1)
ginger1 = ForagableItem("resources/sprites/ginger.png", "resources/sprites/mound.png", 220, 300, "ginger", 1)
ginger2 = ForagableItem("resources/sprites/ginger.png", "resources/sprites/mound.png", 380, 350, "ginger", 1)
player = Player("resources/sprites/doctor.png")

all_sprites = pygame.sprite.Group()

all_sprites.add(tree1)
all_sprites.add(tree2)
all_sprites.add(ginger1)
all_sprites.add(ginger2)
all_sprites.add(player)

font = pygame.font.Font('freesansbold.ttf', 24)

running = True
inventory_showing = False

while running:

    # process events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYUP:
            if event.key == K_i:
                inventory_showing = not inventory_showing

    # get key inputs
    pressed_keys = pygame.key.get_pressed()


    if not inventory_showing:
        player.update(pressed_keys, all_sprites)


    # background
    screen.fill((0, 205, 249))
    pygame.draw.rect(screen, (51, 152, 75), pygame.Rect(0, 300, 500, 200))

    # foragable items
    for entity in all_sprites:
        screen.blit(entity.surf, entity.rect)

    screen.blit(player.surf, player.rect)

    # inventory menu
    if inventory_showing:
        pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(100, 100, 300, 300))
        text = ''
        x = 105
        y = 105
        for name, val in player.inventory.items():
            text = '{0}:{1} '.format(name, val)
            item_list = font.render(text, True, 'black')
            screen.blit(item_list, (x, y))
            y += 30

    pygame.display.flip()

pygame.quit()
