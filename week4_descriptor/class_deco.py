def deco(a_class):

    class Proxy:
        g = 10

        def __init__(self, * args):
            print(' in Proxy Class')
            self.wrapped = a_class(*args)

        def __getattr__(self, item):
            print(' in __getattr__')
            return getattr(self.wrapped, item)

    return Proxy


@deco
class C:
    def __init__(self, a, b):
        print(' in C class')
        self.a = a
        self.b = b


x = C(12, 13)  # same as C = deco(C)
print(x.g)
print(x.a)     # Not exist in Proxy, but __getattr would do "attribute resolution" to find a in class C (self.wrapped)

