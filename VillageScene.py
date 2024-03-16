import pygame
from pygame.locals import (
    K_i
)
from Scene import Scene
from ForagableItem import ForagableItem
from Player import Player
from Item import Item
from VillagerInteraction import VillagerInteraction


class VillageScene(Scene):
    def __init__(self):
        Scene.__init__(self)
        self.inventory_showing = False
        self.font = pygame.font.Font('freesansbold.ttf', 24)
        self.player = Player("resources/sprites/doctor.png")
        self.house1 = Item("resources/sprites/VillageSceneSprites/house.png", 260, 50)
        # self.elder1 = Item("resources/sprites/VillageSceneSprites/villager.png", 300, 250)
        # elder classified as Item for now
        self.recipe1 = VillagerInteraction("resources/sprites/VillageSceneSprites/villagerRecipe.png", "resources/sprites/VillageSceneSprites/villager3.png", 440, 250, "Recipe", 1)
        self.all_sprites = pygame.sprite.Group()

        self.all_sprites.add(self.house1)
        # self.all_sprites.add(self.elder1)
        self.all_sprites.add(self.recipe1)
        self.all_sprites.add(self.player)


    def update(self, events, pressed_keys):
        for event in events:
            if event.type == pygame.KEYUP:
                if event.key == K_i:
                    self.inventory_showing = not self.inventory_showing

        if not self.inventory_showing:
            self.player.update(pressed_keys, self.all_sprites)

    def render(self, screen):
        screen.fill((0, 251, 249))
        pygame.draw.rect(screen, (51, 152, 75), pygame.Rect(0, 300, 500, 200))

        # Item and Villager Interaction
        for entity in self.all_sprites:
            screen.blit(entity.surf, entity.rect)

        # player
        screen.blit(self.player.surf, self.player.rect)

        # inventory menu
        if self.inventory_showing:
            pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(100, 100, 300, 300))
            text = ''
            x = 105
            y = 105
            for name, val in self.player.inventory.items():
                text = '{0}:{1} '.format(name, val)
                item_list = self.font.render(text, True, 'black')
                screen.blit(item_list, (x, y))
                y += 30
