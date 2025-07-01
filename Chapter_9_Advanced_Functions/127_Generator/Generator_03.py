def sub_generator(x):
    for i in range(x):
        yield i ** 2

def gen(y):
    yield from sub_generator(y)

for num in gen(15):
    print(num)
