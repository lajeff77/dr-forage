import pygame
from pygame.locals import (
    K_h
)

from CuttableItem import CuttableItem
from Item import Item
from MiniGame import MiniGame
from ProgressBar import ProgressBar


class CuttingMiniGame(MiniGame):

    def __init__(self, item):
        super().__init__()
        self.font = pygame.font.Font('freesansbold.ttf', 24)
        self.cutting_board = Item("resources/sprites/cutting-board.png", 0, 200)
        x, y = pygame.mouse.get_pos()
        self.item = item # cuttable item like ginger or lemon
        self.knife = Item("resources/sprites/knife.png", x, y)
        self.click_count = 0
        self.progress_bar = ProgressBar(max_progress=item.get_chop_count(), x=110, y=160)
        self.all_sprites = pygame.sprite.Group()
        self.all_sprites.add(self.cutting_board)
        self.all_sprites.add(self.item)
        self.all_sprites.add(self.knife)

    def update(self, events, keys_pressed):
        for event in events:
            if event.type == pygame.KEYUP:
                if event.key == K_h:
                    self.scene_manager.switch_to_scene("forest")
            if event.type == pygame.MOUSEBUTTONUP:
                self.click_count += 1

        x, y = pygame.mouse.get_pos()
        self.knife.set_pos(x, y)
        self.item.update(self.click_count)
        if not self.progress_bar.is_complete():
            self.progress_bar.set_progress(self.click_count)
        self.progress_bar.update()

        if self.click_count >= self.item.get_chop_count():
            self.success = True
            self.complete = True

    def render(self, screen):
        # background
        screen.fill((191, 111, 74))

        # words
        text = 'chop'
        title = self.font.render(text, True, 'black')
        screen.blit(title, (105, 105))

        text = 'click count {}'.format(self.click_count)
        title = self.font.render(text, True, 'black')
        screen.blit(title, (105, 135))

        # progress bar
        self.progress_bar.render(screen)

        # draw items
        for item in self.all_sprites:
            screen.blit(item.surf, item.rect)
