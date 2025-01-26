class Robot:
    def __init__(self, name):
        self.name = name
        # private property
        self.__age = 25
    
    # private method
    def __this_is_private(self):
        print("Hello from private method")
    
    def greet(self):
        print("Hi, I am a robot")
        self.__this_is_private()

my_robot = Robot("Wilson")
my_robot.greet()