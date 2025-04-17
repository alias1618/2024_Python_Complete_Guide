try:
    f = open("testfile.txt")
    f.write("Write a test line.")
except TypeError:
    print("There is a type error")
except OSError:
    print("There is a OS error")
except:
    print("Whatever other errors will go here")
finally:
    print("This will run no matter what.")