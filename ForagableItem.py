import pygame

from pygame.locals import (
    RLEACCEL
)

#sprite_img_path = relative path
class ForagableItem(pygame.sprite.Sprite):
    def __init__(self, sprite_img_path, death_img_path, x, y, name, count):
        super(ForagableItem, self).__init__()
        self.surf = pygame.image.load(sprite_img_path)
        self.surf.set_colorkey((255,255,255), RLEACCEL)
        self.rect = self.surf.get_rect()
        self.rect.left = x
        self.rect.top = y
        self.death_img_path = death_img_path
        self.name = name
        self.count = count
        self.collected = False

    def collide(self):
        temp_x = self.rect.left
        temp_y = self.rect.top
        self.surf = pygame.image.load(self.death_img_path)
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        self.rect = self.surf.get_rect()
        self.rect.left = temp_x
        self.rect.top = temp_y
        self.collected = True
