import pygame

from pygame.locals import (
    RLEACCEL
)

class Item(pygame.sprite.Sprite):
    def __init__(self, sprite_img_path, x, y):
        super(Item, self).__init__()
        self.surf = pygame.image.load(sprite_img_path)
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        self.rect = self.surf.get_rect()
        self.set_pos(x, y)

    def set_x(self, x):
        self.rect.left = x

    def set_y(self, y):
        self.rect.top = y

    def set_pos(self, x, y):
        self.rect.left = x
        self.rect.top = y
