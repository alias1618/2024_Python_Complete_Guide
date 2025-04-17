try:
    with open("hello.txt") as f:
        print(f.read())
except FileNotFoundError:
    print("File not found....")