a = 10

# parameters (input) are local variables in the function

def change(num):
    global a
    num = 25

change(a)
print(a)