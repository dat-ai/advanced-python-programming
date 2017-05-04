
def tracer(func):
    def oncall(*args):
        oncall.calls += 1
        print('call %s to %s' % (oncall.calls, func.__name__))
        return func(*args)
    oncall.calls = 0
    return oncall


class C:
    @tracer # spam = tracer
    def spam(self, a, b, c):
        return a + b + c

class D:
    @tracer # spam = tracer
    def spam2(self, a, b, c):
        return a - b - c

@tracer
def func(x, y):
    print(x + y)
    return "This is Func"

test = C()
test2 = D()

print(test.spam(10, 12, 13))    # equal to test oncall(10, 12, 13)
print(test2.spam2(10, 20, 30))   # equal to test oncall(10, 12, 13)
print(func(3, 4))



