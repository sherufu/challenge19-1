class Hexagon:
    def __init__(self, side):
        self.side = side

    def calcurate_perimeter(self):
        return self.side * 6


print(Hexagon(3).calcurate_perimeter())
