class Triangle():
    def __init__(self, tall, bottom):
        self.tall = tall
        self.bottom = bottom


    def area(self):
        return self.tall * self.bottom / 2


triangle = Triangle(2, 4)
print(triangle.area())
