def myfunc(*args, **kwargs):
    print("I would like to eat {} {}".format(args[1], kwargs["food"]))


myfunc(14, 17, 23, "Hello", name="Wilson", food="eggs")