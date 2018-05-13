import math

class Triangle:
    def __init__(self, width, height):
        self.width = float(width)
        self.height = float(height)

    def area(self):
        return self.width * self.height / 2


t = Triangle(4, 4)
print(t.area())
