class E:
    pass

class F:
    def do_stuff(self):
        print("doing stuff from F")

class G:
    def do_stuff(self):
        print("doing stuff from G")

class B(E, F):
    pass

class C:
    def do_stuff(self):
        print("doing stuff from C")

class D(G):
    pass

class A(B, C, D):
    pass

a = A()
a.do_stuff()

