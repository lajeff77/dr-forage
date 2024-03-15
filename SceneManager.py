
class SceneManager:

    def __init__(self):
        self.scenes = {}
        self.current_scene = None

    def add_scene(self, name, scene):
        self.scenes[name] = scene

    def switch_to_scene(self, name):
        if name in self.scenes:
            self.current_scene = self.scenes[name]
        else:
            print('scene {} not found'.format(name))

    def get_current_scene(self):
        return self.current_scene
