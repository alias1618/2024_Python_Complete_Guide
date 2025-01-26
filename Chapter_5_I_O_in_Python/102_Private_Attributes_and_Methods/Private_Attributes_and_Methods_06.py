class Robot:
    def __init__(self, name):
        self.name = name
        # private property
        self.__age = 25
    
    def age_setter(self, new_age):
        if new_age > 0 and new_age < 100:
            self.__age = new_age
        else:
            print("New age setting is invalid")

    def age_getter(self):
        print(self.__age)

my_robot = Robot("Wilson")
my_robot.age_setter(-30)
my_robot.age_getter()