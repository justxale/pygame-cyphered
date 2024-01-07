import pygame
from cyphered.data.constants import SCREEN_SIZE


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

    def switch_scene(self, scene, fade=False, save=False):
        if fade:
            self.parent_scene.fade_and_switch_scene(scene)
        else:
            if save:
                self.parent_scene.switch_scene(scene, self)
            else:
                self.parent_scene.switch_scene(scene)

    def destroy(self):
        self.on_destroy()
        self.need_to_render = False
        self.parent_scene.subscene = None

    def on_destroy(self):
        pass


class TransitionSubscene(BaseSubscene):
    def __init__(self, parent, scene_to_switch):
        super().__init__(parent)
        self.fadein = True
        self.finished = False
        self.next_scene = scene_to_switch
        self.progress = 0.0

    def render(self, screen):
        s = pygame.Surface(SCREEN_SIZE)
        s.set_alpha(int(256 * self.progress))
        s.fill((0, 0, 0))
        screen.blit(s, (0, 0))
        if self.fadein:
            self.progress += 0.01
            if self.progress >= 1.0:
                self.finished = True
        else:
            self.progress -= 0.01
            if self.progress <= 0.0:
                self.finished = True
        if self.finished:
            self.switch_scene(self.next_scene, save=True)
            self.finished = False
            self.fadein = False
        if self.progress <= 0.0 and not self.fadein:
            print('TransitionSubscene destroyed')
            self.destroy()

    def destroy(self):
        self.on_destroy()
        self.need_to_render = False
        self.parent_scene.subscene = None
        self.next_scene.subscene = None


class BaseScene:
    def __init__(self):
        self.is_paused = False
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

    def fade_and_switch_scene(self, scene_to_switch):
        trans = TransitionSubscene(self, scene_to_switch)
        self.open_subscene(trans)

    def switch_scene(self, scene_to_switch, subscene=None):
        self.on_destroy()
        self.next = scene_to_switch
        if scene_to_switch is not None:
            self.next.subscene = subscene

    def open_subscene(self, subscene: BaseSubscene, pause=False):
        if pause:
            self.is_paused = True
        self.subscene = subscene

    def destroy(self):
        self.on_destroy()
        self.switch_scene(None)

    def on_destroy(self):
        pass
