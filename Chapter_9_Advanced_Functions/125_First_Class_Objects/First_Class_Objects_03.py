def square(num):
    return num ** 2

my_list = [1, 2, 3, 4]
result = map(square, my_list)
for i in result:
    print(i)