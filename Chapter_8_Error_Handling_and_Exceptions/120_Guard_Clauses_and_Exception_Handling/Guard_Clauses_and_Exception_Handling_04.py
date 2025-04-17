def divide(a, b):
    if type(a) != int or type(b) != int:
        raise ValueError("Not valid type given!!")
    
    if b == 0:
        raise ZeroDivisionError("Second argument cannot be 0")
    
    return a / b


try:
    # print(divide(10, "hello"))
    print(divide(10, 0))
    print(divide(6, 3))
except Exception as e:
    print(e)