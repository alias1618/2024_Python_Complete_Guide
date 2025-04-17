try:
    f = open("testfile.txt", "w")
    f.write("Write a test line.")
except TypeError:
    print("There is a type error")
except OSError:
    print("There is a OS error")
finally:
    print("This will run no matter what.")