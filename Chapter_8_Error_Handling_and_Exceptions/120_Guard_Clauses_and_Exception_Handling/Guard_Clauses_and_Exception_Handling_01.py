def divide(a, b):
    if type(a) == int and type(b) == int:
        if b != 0:
            return a / b
        else:
            return "The second argument cannot be 0."
    else:
        return "Invalid argument type!!"
    
print(divide(10, "hello"))
print(divide(10, 0))
print(divide(6, 3))