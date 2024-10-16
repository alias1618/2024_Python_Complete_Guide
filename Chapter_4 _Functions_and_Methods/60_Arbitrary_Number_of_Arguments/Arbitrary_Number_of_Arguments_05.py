def myfunc(**kwargs):
    print("{} is now {} years old.".format(kwargs["name"], kwargs["age"]))


myfunc(name="Wilson", age=25, address="Hawaii")