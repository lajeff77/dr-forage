import pygame


class ProgressBar:

    def __init__(self, max_progress, x, y, color1=(255, 235, 87), color2=(19, 19, 19)):
        self.max_progress = max_progress
        self.progress = 0
        self.x = x
        self.y = y
        self.color1 = color1  # inside of progress bar
        self.color2 = color2  # outline
        self.complete = False  # indicates if progress bar is filled all the way

    def is_complete(self):
        return self.complete

    def set_progress(self, progress):
        self.progress = progress

    def update(self):
        if self.progress >= self.max_progress:
            self.complete = True

    def render(self, screen):
        # draw inside
        pygame.draw.rect(screen, self.color1, pygame.Rect(self.x, self.y, self.max_progress * self.progress, 20))
        # draw outline
        pygame.draw.rect(screen, self.color2, pygame.Rect(self.x, self.y, self.max_progress * self.max_progress, 20), 1)
