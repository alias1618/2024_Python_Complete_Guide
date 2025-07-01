def hello():
    def greet():
        print("greet!!")
    return greet

welcome = hello()
welcome()