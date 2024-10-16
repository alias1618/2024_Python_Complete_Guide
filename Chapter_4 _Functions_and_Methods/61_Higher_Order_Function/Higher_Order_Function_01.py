def higherOrder(fn):
    fn()

def smallfunc():
    print("Hello from small function")

higherOrder(smallfunc)