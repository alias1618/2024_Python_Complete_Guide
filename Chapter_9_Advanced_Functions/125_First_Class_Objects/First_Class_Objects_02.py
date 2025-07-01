def hello():
    print("Hello World")

def call_another_function(other_func):
    # other_func = hello
    other_func()

call_another_function(hello)