def sum(*args):
    result = 0
    for number in range(0, len(args)):
        print(f"We are now at number {number}")
        print(f"Also, args[number] is {args[number]}.")
        result += args[number]
        print(f"Now, the result is {result}")
    return result


print(sum(44, 22, 18, 3, -5, 44, -1000))