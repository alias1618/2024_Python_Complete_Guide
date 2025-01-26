class Robot:
    def __init__(self, name):
        self.name = name
        # private property
        self.__age = 25

my_robot = Robot("Wilson")
print(my_robot.__age)