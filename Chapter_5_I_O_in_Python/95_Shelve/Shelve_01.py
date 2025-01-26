import shelve

integers1 = [1, 2, 3, 4, 5, 6]
integers2 = [6, 7, 8, 9, 10]
integers3 = [100, 101, 102, 103]

# c 代表create
with shelve.open("Chapter_5_I_O_in_Python/95_Shelve/shelf-example", "c") as shelf:
    shelf['ints1'] = integers1
    shelf['ints2'] = integers2
    shelf['ints3'] = integers3