import math
import pygame

from .loop_imports import LoopImports
from ..complex_number import ComplexNumber

from ..PreCodedSignals.christmas_tree import CHRISTMAS_TREE_SIGNAL
from ..PreCodedSignals.heart import HEART_SIGNAL


class Loop:

    def __init__(self):
        self.signal = HEART_SIGNAL

        pygame.init()
        self.screen = pygame.display.set_mode((1200, 750))
        self.loop_imports = LoopImports(self)

        self.clock = pygame.time.Clock()
        self.running = True

        self.dt = 2 * math.pi / len(self.signal)

    def run(self):
        while self.running:
            self.events()
            self.update()
            self.draw()
            self.clock.tick(30)

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def update(self):
        self.loop_imports.update(self.dt)

    def draw(self):
        self.screen.fill((0, 0, 0))
        self.loop_imports.draw()
        pygame.display.flip()
