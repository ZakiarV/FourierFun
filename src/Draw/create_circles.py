import pygame

from .circle import Circle, Point
from ..FourierCalculations.calculate import calculate


def create_circles(signal) -> list[Circle]:
    circles = []
    circle_numbers = calculate(signal)
    for i in range(len(circle_numbers)):
        if len(circles) < 1:
            circles.append(Circle(circle_numbers[i][0], circle_numbers[i][1], circle_numbers[i][2]))
        else:
            circles.append(Circle(circle_numbers[i][0], circle_numbers[i][1], circle_numbers[i][2], circles[i - 1]))
    return circles
