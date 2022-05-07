a = 5

def f(a=4):
    b = 4
    print(globals())
    print(locals())
    print(a)
    print(b)

class A:
    a = 9
    a += 1
    print(a)
    print(globals())
    print(locals())
    