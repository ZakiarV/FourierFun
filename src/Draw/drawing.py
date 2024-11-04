import math
import pygame

from .create_circles import create_circles


class Path:
    def __init__(self):
        self.path = []

    def draw(self, screen):
        if len(self.path) > 1:
            pygame.draw.lines(screen, (255, 0, 255), False, self.path, 1)
        else:
            pygame.draw.circle(screen, (255, 0, 255), self.path[0], 1, 1)

    def update(self, x, y):
        self.path.append((x, y))


class Draw:
    def __init__(self, signal):
        self.signal = signal
        self.circles = create_circles(signal)
        self.path = Path()
        self.rotation = 0

    def draw(self, screen):
        for circle in self.circles:
            circle.draw(screen)
        self.path.draw(screen)

    def update(self, dt):
        self.rotation += dt
        if self.rotation >= 2 * math.pi:
            self.rotation = 0
            self.path.path = []
        for circle in self.circles:
            circle.update(dt)
        self.path.update(self.circles[-1].point.x, self.circles[-1].point.y)


def draw(signal):
    return Draw(signal)