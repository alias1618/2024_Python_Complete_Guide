a = [1, 2, 3, 4]

# parameters (input) are local variables in the function

def change(lst):
    lst[0] = 100

change(a)
print(a)