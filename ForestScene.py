import pygame
from pygame.locals import (
     K_i, K_h
)
from Scene import Scene
from ForagableItem import ForagableItem
from Player import Player


class ForestScene(Scene):

    def __init__(self, scene_manager):
        Scene.__init__(self, scene_manager)
        self.inventory_showing = False
        self.font = pygame.font.Font('freesansbold.ttf', 24)
        self.tree1 = ForagableItem("resources/sprites/lemon-tree.png", "resources/sprites/tree.png", 250, 120, "lemon", 3)
        self.tree2 = ForagableItem("resources/sprites/honey-tree.png", "resources/sprites/tree.png", 50, 150, "honey", 1)
        self.ginger1 = ForagableItem("resources/sprites/ginger-plant.png", "resources/sprites/mound.png", 220, 300, "ginger", 1)
        self.ginger2 = ForagableItem("resources/sprites/ginger-plant.png", "resources/sprites/mound.png", 380, 350, "ginger", 1)
        self.player = Player("resources/sprites/doctor.png")
        self.all_sprites = pygame.sprite.Group()

        self.all_sprites.add(self.tree1)
        self.all_sprites.add(self.tree2)
        self.all_sprites.add(self.ginger1)
        self.all_sprites.add(self.ginger2)
        self.all_sprites.add(self.player)

    def update(self, events, pressed_keys):
        for event in events:
            if event.type == pygame.KEYUP:
                if event.key == K_i:
                    self.inventory_showing = not self.inventory_showing
                if event.key == K_h:
                    self.scene_manager.switch_to_scene("workstation")

        if not self.inventory_showing:
            self.player.update(pressed_keys, self.all_sprites)


    def render(self, screen):
        # background
        screen.fill((0, 205, 249))
        pygame.draw.rect(screen, (51, 152, 75), pygame.Rect(0, 300, 500, 200))

        # draw all sprites
        for entity in self.all_sprites:
            screen.blit(entity.surf, entity.rect)

        # inventory menu
        if self.inventory_showing:
            pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(100, 100, 300, 300))
            text = 'inventory'
            title = self.font.render(text, True, 'black')
            screen.blit(title, (105, 105))
            x = 105
            y = 135
            for name, val in self.player.inventory.items():
                text = '{0}:{1} '.format(name, val)
                item_list = self.font.render(text, True, 'black')
                screen.blit(item_list, (x, y))
                y += 30