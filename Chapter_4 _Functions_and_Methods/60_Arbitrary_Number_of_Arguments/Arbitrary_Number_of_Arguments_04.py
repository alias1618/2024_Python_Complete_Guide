def myfunc(**kwargs):
    print(kwargs)
    print(type(kwargs))

myfunc(name="Wilson", age=25, address="Hawaii")