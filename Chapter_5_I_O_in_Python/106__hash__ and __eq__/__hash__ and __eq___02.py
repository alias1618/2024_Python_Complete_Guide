class Robot:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address
    
    # define a private method __key()
    def __key(self):
        return (self.name, self.age, self.address)
    
    # implement __hash__() function
    def __hash__(self):
        return hash(self.__key())

robot1 = Robot("Wilson", 25, "Taiwan")
robot2 = Robot("Grace", 26, "Hawaii")
print(robot1 == robot2)

