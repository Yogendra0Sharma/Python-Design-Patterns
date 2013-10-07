# http://stackoverflow.com/questions/3118929/implementing-the-decorator-pattern-in-python


class foo(object):
    def f1(self):			# normal function
        print("original f1")

    def f2(self):			# normal function
        print("original f2")


class foo_decorator(object):
    def __init__(self, decoratee):  # Constructor of class foo_decotrator and it take one argument.
        self._decoratee = decoratee  # self._decoratee is private member it can be access by only class mamber function.
									# self._decoratee is a refrence to foo class object.
    def f1(self):
        print("decorated f1")
        self._decoratee.f1()   # u.f1()

    def __getattr__(self, name):    #magic function or decorator.
        return getattr(self._decoratee, name)

u = foo()   #create a object of class foo
v = foo_decorator(u) #create a object of foo_decorator class and pass a perameter as class foo object
v.f1()   # its print out decorator f1 and origenal f1
v.f2()
