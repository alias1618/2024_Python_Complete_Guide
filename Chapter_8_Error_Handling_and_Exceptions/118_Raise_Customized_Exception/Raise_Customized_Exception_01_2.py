class NegativeNumberException(RuntimeError):
    def __init__(self, age):
        super().__init__()
        self.age = age
        if(age < 0):
            print("This is not a valid age!!!")

def enter_age(age):
    if age < 0:
        raise NegativeNumberException(age)
    
    if age % 2 == 0:
        print("Your age is an even number")
    else:
        print("Your age is odd.")