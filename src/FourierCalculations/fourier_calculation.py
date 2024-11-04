import math

from src.complex_number import ComplexNumber


class FourierCalculation:
    def __init__(self, signal):
        self.signal = signal
        self.n = len(signal)

    def calculate(self):
        fourier = []
        for k in range(self.n):
            sum_s = ComplexNumber(0, 0)
            for t in range(self.n):
                angle = 2 * math.pi * t * k / self.n
                sum_s += (ComplexNumber(self.signal[t].real, self.signal[t].imaginary) * ComplexNumber(math.cos(angle), -math.sin(angle)))
            sum_s.real /= self.n
            sum_s.imaginary /= self.n
            fourier.append((sum_s, k))
        return fourier
