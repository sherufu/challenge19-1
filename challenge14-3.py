class Square:
    square_list = []

    def __init__(self, width, height):
        self.w = width
        self.h = height
        self.square_list.append(self)

    def __repr__(self):
        return str(self.w) + "by" + str(self.h) + "by" + str(self.w) + "by" + str(self.h)


def equal(c1, c2):
    return c1 is c2


s1 = Square(1, 2)
s2 = Square(1, 2)
print(equal(s1, s2))
print(equal(s1, s1))
