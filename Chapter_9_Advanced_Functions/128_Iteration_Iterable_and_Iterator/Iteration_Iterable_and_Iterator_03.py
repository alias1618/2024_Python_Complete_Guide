# iterable => (1) __iter__() method return an iterator
# iterable => (2) implements __getitem__()

class Building(object):
    def __init__(self, floors):
        self.__floors = [None] * floors

    def __setitem__(self, floor_number, data):
        self.__floors[floor_number] = data

    def __getitem__(self, floor_number):
        return self.__floors[floor_number]
    
building1 = Building(4)
building1[0] = 'Reception'
building1[1] = 'ABC Corp'
building1[2] = 'DEF Inc'

for thing in building1:
    print(thing)