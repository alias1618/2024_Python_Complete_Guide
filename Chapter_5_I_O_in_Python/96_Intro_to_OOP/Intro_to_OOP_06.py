class Robot:
    # in classes, we can also define doctring
    """Robot class is for creating robots"""
    # contructor
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        print(f"{self.name} is walking...")

my_robot_1 = Robot("Wilson", 25)
my_robot_2 = Robot("Grace", 26)
my_robot_2.walk()