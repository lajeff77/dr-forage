class Scene:
    def __init__(self):
        self.next = self

    def update(self, events, pressed_keys):
        pass

    def render(self, screen):
        pass

    def switch_to_Scene(self, next_scene):
        self.next = next_scene

    def terminate(self):
        self.switch_to_scene(None)
