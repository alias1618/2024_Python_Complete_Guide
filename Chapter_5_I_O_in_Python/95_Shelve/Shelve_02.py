import shelve

# c 代表create
with shelve.open("Chapter_5_I_O_in_Python/95_Shelve/shelf-example", "r") as shelf:
    for key in shelf.keys():
        print(key)
    print(shelf['ints2'])