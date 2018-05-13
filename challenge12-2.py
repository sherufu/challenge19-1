import math

class Circle:
    def __init__(self, diameter):
        self.diameter = float(diameter)

    def area(self):
        return self.diameter * math.pi


c = Circle(4)
print(c.area())
