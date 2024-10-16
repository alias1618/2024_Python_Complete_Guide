def even(num):
    return num % 2 == 0
    # if num % 2 == 0:
    #     return True
    # else:
    #     return False

myList = [444532, 3211543, -998432, 66154]

for item in filter(even, myList):
    print(item)