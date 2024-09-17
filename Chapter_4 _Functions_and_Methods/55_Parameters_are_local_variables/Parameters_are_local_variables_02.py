# global variables, local variables

a = 5   # global variable



def f1():
    x = 2
    y = 3
    print(x, y, a)

def f2():
    x = 10
    y = 17
    print(x, y, a)

f1()