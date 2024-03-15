from Item import Item
import pygame

class CuttableItem(Item):

    def __init__(self, img, chopped_img, x, y, chop_count):
        super().__init__(img, x, y)
        self.chop_count = chop_count
        self.chopped_img = chopped_img
        self.done_chopping = False

    def get_chop_count(self):
        return self.chop_count

    def update(self, clicks):
        if clicks >= self.chop_count:
            self.done_chopping = True
            self.surf = pygame.image.load(self.chopped_img)
