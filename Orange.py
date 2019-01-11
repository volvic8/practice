class Orange:
    def __init__(self, w, c):
        self.weight = w
        self.color = c
        self.mold = 0
        print("Created!")

    def rot(self, days, temp):
        """temp(温度)は摂氏"""
        self.mold = days * temp

or1 = Orange(10, "dark orange")
print(or1.mold)
or1.rot(3, 37)
print(or1.mold)
