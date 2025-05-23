class Circles:
    """This class creates circle"""
    pi = 3.14159
    all_circles = []

    def __init__(self, radius):
        self.radius = radius
        self.__class__.all_circles.append(self)

    def area(self):
        return self.__class__.pi * (self.radius ** 2)
    
    @staticmethod
    def total_area():
        total = 0
        for circle in Circle.all_circles:
            total += circle.area()
        return total
    
    @classmethod
    def total_area2(cls):
        total = 0
        for circle in cls.all_circles:
            total += circle.area()
        return total
    
c1 = Circles(10)
c2 = Circles(15)
# print(c1.__class__.total_area())
print(c1.__class__.total_area2())