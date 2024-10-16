# myfunc(*whatever, **kw):  myfunc內的字體可以隨意更換
def myfunc(*whatever, **kw):
    print("I would like to eat {} {}".format(whatever[1], kw["food"]))


myfunc(14, 17, 23, "Hello", name="Wilson", food="eggs")