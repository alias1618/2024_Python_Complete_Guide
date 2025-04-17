import one_02

print("We are running codes in two,py now.")

def get__name():
    print(__name__)

if __name__ == '__main__':
    print("We are running two.py directly.")
    get__name()
    one_02.get_name()