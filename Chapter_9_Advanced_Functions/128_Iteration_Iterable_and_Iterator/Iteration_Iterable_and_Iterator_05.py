# iterator is a subset of iterable

x = [1, 2, 3]
# print(dir(x))   # List is not iterator
# # __iter__() return a iterator

print(dir(iter(x)))