class BaseSubscene:
    def __init__(self, parent_scene: 'BaseScene'):
        self.need_to_render = True
        self.parent_scene = parent_scene

    def update(self, screen):
        if self.need_to_render:
            self.render(screen)

    def process_events(self, events):
        pass

    def render(self, screen):
        if not self.need_to_render:
            return

    def switch_subscene(self, subscene):
        self.parent_scene.subscene = subscene

    def switch_scene(self, scene, destroy=False):
        if destroy:
            self.destroy()
        self.parent_scene.switch_scene(scene)

    def destroy(self):
        self.on_destroy()
        self.need_to_render = False
        self.parent_scene.subscene = None

    def on_destroy(self):
        pass


class BaseScene:
    def __init__(self):
        self.next: BaseScene = self
        self.subscene: BaseSubscene | None = None

    def update(self, screen):
        self.render(screen)
        if self.subscene:
            self.subscene.update(screen)

    def process_events(self, events):
        if self.subscene:
            self.subscene.process_events(events)

    def render(self, screen):
        pass

    def switch_scene(self, scene_to_switch):
        self.on_destroy()
        self.next = scene_to_switch

    def open_subscene(self, subscene: BaseSubscene):
        self.subscene = subscene

    def destroy(self):
        self.on_destroy()
        self.switch_scene(None)

    def on_destroy(self):
        pass
