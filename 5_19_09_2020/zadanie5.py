class A(object):
    def func(self):
        print('A')
    def func_from_a(self):
        print('hello, I am in A')

class B(A):
    def func(self):
        print('B')
    def func_from_b(self):
        print('hello, I am in B')

a = A()
b = B()

a.func()
b.func()

b.func_from_a()
b.func_from_b()

a.func_from_a()
a.func_from_b()