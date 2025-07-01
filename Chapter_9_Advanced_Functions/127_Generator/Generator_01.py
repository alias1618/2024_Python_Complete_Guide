def cube(n):
    result = []
    for x in range(n):
        result.append(x ** 3)
    return result

for i in cube(10):
    print(i)
    