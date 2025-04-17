try:
    lst = [1, 2, 3]
    print(lst[4])
except IndexError:
    print("There is an index error")
except LookupError:
    print("There is a look up error")

    