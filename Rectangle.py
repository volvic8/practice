class Rectangle():
    def __init__(self, height, width):
        self.height = height
        self.width = width

    def calculate_perimeter(self):
        return self.height * self.width

class Square():
    def __init__(self, side):
        self.side = side

    def calculate_perimeter(self):
        return self.side ** 2

    def change_size(self, addValue):
        self.side += addValue
        
rectangle = Rectangle(2, 3)
print(rectangle.calculate_perimeter())

square = Square(2)
print(square.calculate_perimeter())

square.change_size(3)
print(square.calculate_perimeter())
