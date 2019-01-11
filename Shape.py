class Shape():
    def what_am_i(self):
        print("I am a shape")

class Rectangle(Shape):
    def __init__(self, height, width):
        self.height = height
        self.width = width

    def calculate_perimeter(self):
        return self.height * self.width

class Square(Shape):

    square_list = []

    def __init__(self, side):
        self.side = side
        self.square_list.append(self)

    def calculate_perimeter(self):
        return self.side ** 2

    def change_size(self, addValue):
        self.side += addValue

    def __repr__(self):
        return "{} by {} by {} by {}".format(self.side, self.side, self.side, self.side)

rectangle = Rectangle(2, 3)
rectangle.what_am_i()

square = Square(2)
square.what_am_i()

print(square)
