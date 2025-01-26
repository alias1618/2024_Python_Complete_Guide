# 3.Write a function called "position" that returns a tuple of the first uppercase letter and its index location. If not found, returns -1.


# output
    # position("abcd")  # returns -1
    # position("AbcD")  # returns ('A', 0)
    # position("abCD")  # returns ('C', 2)

def position(str):
    tuple1=False
    # tuple1 = tuple(str)
    # print(len(text))
    for index, item in enumerate(str):
        if item.isupper():
            tuple1 = (item, index)
            if tuple1:
                break
        
    if tuple1:
        print(tuple1)
    else:
        print(-1)


position("abcd")  # returns -1
position("AbcD")  # returns ('A', 0)
position("abCD")  # returns ('C', 2)