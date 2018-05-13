class Square:
    square_list = []

    def __init__(self, width, height):
        self.w = width
        self.h = height
        self.square_list.append(self)


s1 = Square(1, 2)
s2 = Square(2, 4)
s3 = Square(3, 6)

print(Square.square_list)
