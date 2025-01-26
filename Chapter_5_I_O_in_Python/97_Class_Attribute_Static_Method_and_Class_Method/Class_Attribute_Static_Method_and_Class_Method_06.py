class Robot:
    ingredient = "metal"

    def __init__(self, name, age):
        self.name = name
        self.age = age


    @staticmethod
    def greet():
        print("A robot says hi...")

my_robot_1 = Robot("Wilson", 25)
my_robot_2 = Robot("Grace", 26)

# my_robot_1.sleep(15)

Robot.greet()
my_robot_1.__class__.greet()