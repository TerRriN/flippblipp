a = 3
b = 14

def double(x):
    return 2*x

def triple(x):
    return 3*x

def quadruple(x):
    return double(x) + double(x)

def funky(x, y):
    return triple(x) + quadruple(y)

d1 = double(a)
d2 = double(b)

t1 = triple(a)
t2 = triple(b)

q1 = quadruple(a)
q2 = quadruple(b)

f1 = funky(a, b)
f2 = funky(b, b)