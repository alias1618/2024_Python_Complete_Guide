# iterable => __iter__() method return an iterator
# any generator is an iterator
class Somrthing:
    def __iter__(self):
        yield 5 
        for x in range(1, 4):
            yield x

s = Somrthing()
# s is an iterable
# iter(iterable) returns an iterator
print(iter(s))
for i in s:
    print(i)