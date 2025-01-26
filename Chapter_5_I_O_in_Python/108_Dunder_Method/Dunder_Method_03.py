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
            return self.age == other.age
        return NotImplemented
    
    def __len__(self):
        return self.age
    
    def __str__(self):
        return f"{self.name} is now {self.age} years old, living in {self.address}"
    
    def __repr__(self):
        return f"name: {self.name}, age: {self.age}, age: {self.address}"

robot1 = Robot("Wilson", 25, "Taiwan")
robot2 = Robot("Grace", 25, "Hawail")

print(repr(robot1))

