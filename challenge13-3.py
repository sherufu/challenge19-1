class Shape:
    def what_am_i(self):
        return "I am a shape"

class Rectangle(Shape):
    def __init__(self, len):
        self.len = len

    def calculate_perimeter(self):
        return self.len * 4

    def change_size(self, value):
        self.len += value
    

class Triangle(Shape):
    def __init__(self, len):
        self.len = len

    def calculate_perimeter(self):
        return self.len * 3
    

r = Rectangle(3)
t = Triangle(3)
#print(r.calculate_perimeter())
#print(t.calculate_perimeter())

#r.change_size(2)
#print(r.calculate_perimeter())

print(r.what_am_i())
print(t.what_am_i())
