class Robot:
    ingredient = "metal"

    def __init__(self, name, age):
        self.name = name
        self.age = age


    def walk(self):
        print(f"{self.name} is walking...")

    def sleep(self, hours):
        print(f"{self.name} is going to sleep for {hours} hours.")

my_robot_1 = Robot("Wilson", 25)
my_robot_2 = Robot("Grace", 26)

# my_robot_1.sleep(15)

print(Robot.ingredient)