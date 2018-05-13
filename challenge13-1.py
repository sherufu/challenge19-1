class Rectangle:
    def __init__(self, len):
        self.len = len

    def calculate_perimeter(self):
        return self.len * 4

class Triangle:
    def __init__(self, len):
        self.len = len

    def calculate_perimeter(self):
        return self.len * 3

r = Rectangle(3)
t = Triangle(3)
print(r.calculate_perimeter())
print(t.calculate_perimeter())
