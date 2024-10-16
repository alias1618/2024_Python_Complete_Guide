def sum(*args):
    result = 0
    for number in range(0, len(args)):
        result += args[number]
        print(f"Now, the result is {result}")
    return result


print(sum(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))