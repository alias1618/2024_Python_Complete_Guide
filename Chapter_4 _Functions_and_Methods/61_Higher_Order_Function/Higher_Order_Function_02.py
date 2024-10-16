def sqare(num):
    return num ** 2

myList = [-10, 3, 9, 8, 10]
print(map(sqare, myList))

for item in map(sqare, myList):
    print(item)