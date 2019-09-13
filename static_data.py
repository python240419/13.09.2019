
class Circle:
    # class variable - static variable
    __pie = 3.14 # static is loaded when
        # class is loaded into memory
    def __init__(self, radius):
        self.radius = radius
    def getArea(self):
        return Cirlce.pie * radius ** 2

print(Circle.pie)
#Circle.pie = 12
