import math
import pygame


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self, screen):
        pygame.draw.circle(screen, (0, 255, 0), (int(self.x), int(self.y)), 6, 3)

    def update(self, x, y):
        self.x = x
        self.y = y


class Circle:
    def __init__(self, radius, angle, frequency, parent=None):
        self.radius = radius
        self.angle = angle
        self.frequency = frequency
        self.parent = parent

        if self.parent:
            self.x = self.parent.point.x
            self.y = self.parent.point.y
        else:
            self.x = 600
            self.y = 375

        self.point = Point(self.x + self.radius * math.cos(self.angle),
                           self.y + self.radius * math.sin(self.angle))

    def draw(self, screen):
        self.point.draw(screen)
        pygame.draw.line(screen, (0, 0, 255), (self.x, self.y), (self.point.x, self.point.y), 2)

    def update(self, dt):
        self.angle += self.frequency * dt
        self.x = self.parent.point.x if self.parent else 600
        self.y = self.parent.point.y if self.parent else 375
        self.point.update(self.x + self.radius * math.cos(self.angle),
                          self.y + self.radius * math.sin(self.angle))
