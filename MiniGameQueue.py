
class MiniGameQueue:

    def __init__(self, queue):
        self.queue = queue
        self.curr_idx = 0

    def next(self):
        if self.curr_idx < len(self.queue) -1:
            self.curr_idx += 1

    def get_current_minigame(self):
        return self.queue[self.curr_idx]
