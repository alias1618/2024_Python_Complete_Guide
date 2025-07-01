def hello(name):
    def greet(another_name):
        print("hello, " + another_name)

    def bye(another_name):
        print("bye, " + another_name)
    
    if name == "greet":
        return greet
    else:
        return bye

welcome = hello("greet")
goodbye = hello("something else")
welcome("Wilson")
goodbye("Grace")