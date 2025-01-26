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
    
    def __eq__(self, other):
        if isinstance(other, Robot):
            return self.__key() == other.__key()
        return NotImplemented

robot1 = Robot("Wilson", 25, "Taiwan")
robot2 = Robot("Wilson", 25, "Taiwan")
print(robot1 == robot2)

