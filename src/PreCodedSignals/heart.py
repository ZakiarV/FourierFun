import math
from src.complex_number import ComplexNumber

HEART_SIGNAL = [ComplexNumber(-16 * 21 * math.sin(math.radians(t)) ** 3,
                              -13 * 21 * math.cos(math.radians(t)) + 5 * 21 *
                              math.cos(2 * math.radians(t)) + 42 *
                              math.cos(3 * math.radians(t)) + 21 *
                              math.cos(4 * math.radians(t)))
                for t in range(0, 360)]
