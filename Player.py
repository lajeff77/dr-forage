import pygame

from pygame.locals import (
    RLEACCEL,
    K_w, K_s, K_a, K_d,
    K_e, K_i
)

SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500



class Player(pygame.sprite.Sprite):
    def __init__(self, sprite_img_path):
        super(Player, self).__init__()
        self.surf = pygame.image.load(sprite_img_path)
        self.surf.set_colorkey((255,255,255), RLEACCEL)
        self.rect = self.surf.get_rect()
        self.rect.left = 50
        self.rect.top = 250
        self.inventory = {}

    def update(self, pressed_keys, items):
        if pressed_keys[K_w]:
            self.rect.move_ip(0, -5)
        if pressed_keys[K_s]:
            self.rect.move_ip(0, 5)
        if pressed_keys[K_a]:
            self.rect.move_ip(-5, 0)
        if pressed_keys[K_d]:
            self.rect.move_ip(5, 0)
        if pressed_keys[K_e]:
            collected = pygame.sprite.spritecollide(self, items, False)
            for item in collected:
                if item is not self and not item.collected:
                    item.collide()
                    if item.name not in self.inventory:
                        self.inventory[item.name] = item.count
                    else:
                        self.inventory[item.name] += item.count


        # bounds checking
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT