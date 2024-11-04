import math


class CircleCalculation:
    def __init__(self, fourier):
        self.fourier = fourier
        self.n = len(fourier)

    def calculate(self):
        circles = []
        for i in range(self.n):
            radius = math.sqrt(self.fourier[i][0].real ** 2 + self.fourier[i][0].imaginary ** 2)
            angle = math.atan2(self.fourier[i][0].imaginary, self.fourier[i][0].real)
            circles.append((radius, angle, self.fourier[i][1]))
        return circles
