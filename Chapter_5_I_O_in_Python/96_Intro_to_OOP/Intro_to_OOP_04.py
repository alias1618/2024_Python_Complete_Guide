class Robot:
    # contructor
    def __init__(self, inputname, inputage):
        self.name = inputname
        self.age = inputage

my_robot_1 = Robot("Wilson", 25)
my_robot_2 = Robot("Grace", 26)
print(my_robot_1.age < my_robot_2.age)