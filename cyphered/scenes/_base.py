class BaseScene:
    def __init__(self):
        self.next: BaseScene = self

    def update(self):
        pass

    def process_events(self, events):
        pass

    def render(self, screen):
        pass

    def switch_scene(self, scene_to_switch):
        self.next = scene_to_switch

    def destroy(self):
        self.switch_scene(None)
