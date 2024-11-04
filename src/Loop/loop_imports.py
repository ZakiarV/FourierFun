from ..Draw.drawing import draw as draw_circles


class LoopImports:
    def __init__(self, loop):
        self.loop = loop
        self.circle_draw = draw_circles(loop.signal)

    def draw(self):
        self.circle_draw.draw(self.loop.screen)

    def update(self, dt):
        self.circle_draw.update(dt)
