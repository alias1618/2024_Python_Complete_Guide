# iterator is a subset of iterable

x = [1, 2, 3]
list_iterator = iter(x)

print(next(list_iterator))
print(next(list_iterator))
print(next(list_iterator))

for i in x:
    print(i)