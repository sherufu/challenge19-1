class Square:
    square_list = []

    def __init__(self, width, height):
        self.w = width
        self.h = height
        self.square_list.append(self)

    def __repr__(self):
        return str(self.w) + "by" + str(self.h) + "by" + str(self.w) + "by" + str(self.h)

s1 = Square(1, 2)
print(s1)
