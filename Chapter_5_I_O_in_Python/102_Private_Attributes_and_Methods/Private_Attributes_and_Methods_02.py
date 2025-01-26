class Robot:
    def __init__(self, name):
        self.name = name
        # private property
        self.__age = 25
    
    def greet(self):
        print(f"Hi, I am {self.__age} years old.")

my_robot = Robot("Wilson")
my_robot.greet()