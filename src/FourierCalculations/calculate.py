from .fourier_calculation import FourierCalculation
from .circle_calculation import CircleCalculation


def calculate(signal):
    fourier = FourierCalculation(signal).calculate()
    circles = CircleCalculation(fourier).calculate()
    return circles
