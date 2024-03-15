import pygame

from CuttingMiniGame import CuttingMiniGame
from Scene import Scene
from MiniGameQueue import MiniGameQueue
from CuttableItem import CuttableItem


class WorkStationScene(Scene):

    def __init__(self, scene_manager):
        Scene.__init__(self, scene_manager)
        ginger = CuttableItem("resources/sprites/ginger-root.png", "resources/sprites/ginger-slices.png", 200, 250, 10)
        lemon = CuttableItem("resources/sprites/lemon.png", "resources/sprites/cut-lemon.png", 200, 250, 1)
        self.queue = MiniGameQueue([CuttingMiniGame(ginger), CuttingMiniGame(lemon)]) # create a list of the types of minigames you want
        self.minigame = self.queue.get_current_minigame()

    def update(self, events, keys_pressed):
        if self.minigame.is_complete():
            self.queue.next() # move to the next game in the queue when another is complete
        self.minigame = self.queue.get_current_minigame() # updates to current mini game
        self.minigame.update(events, keys_pressed)

    def render(self, screen):
        self.minigame.render(screen)
