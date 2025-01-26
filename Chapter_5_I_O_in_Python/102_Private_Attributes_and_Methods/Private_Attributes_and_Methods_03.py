class Robot:
    def __init__(self, name):
        self.name = name
        # private property
        self.__age = 25
    
    #getter, setter
    def get_age(self):
        return self.__age
    
    def set_age(self):
        self.__age += 1

my_robot = Robot("Wilson")
my_robot.set_age()
print(my_robot.get_age())