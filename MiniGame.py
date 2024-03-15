
class MiniGame:
    def __init__(self):
        self.complete = False
        self.success = False

    def is_complete(self):
        return self.complete

    def is_success(self):
        return self.success

    def update(self, events, keys_pressed):
        pass

    def render(self, screen):
        pass
