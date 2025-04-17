try:
    lst = [1, 2, 3]
    print(lst[4])
except LookupError:
    print("There is a look up error")
except IndexError:
    print("There is an index error")
    