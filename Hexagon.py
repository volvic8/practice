class Hexagon():
    def __init__(self, len):
        self.len = len

    def calculate_perimeter(self):
        return self.len * 6

hexa = Hexagon(5)
print(hexa.calculate_perimeter())
