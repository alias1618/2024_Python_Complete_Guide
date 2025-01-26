# 2.Write a function called "printEvery3" that prints out integers 1, 4, 7, 10, ..., 88.


# output
    # printEvery3();
    # # 1
    # # 4
    # # ... 
    # # 88

def printEvery3():
    i = 1
    while i < 89:
        print(i)
        i = i + 3

printEvery3()