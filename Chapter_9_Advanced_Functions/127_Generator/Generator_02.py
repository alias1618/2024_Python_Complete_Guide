def cube(n):
    for x in range(n):
        yield x ** 3

for element in cube(10):
    print(element)