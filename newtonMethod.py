
from scipy.linalg import det
from scipy.misc import derivative

def fuf(x):
    return x**2 - 10*x + 25

def f(x):
    return x**3 + 2*x**2  + 1


def newTon():
    eps = 0.01
    x = 1
    found = True

    while found:
        # print(y)
        y = x - fuf(x) / derivative(fuf, x, dx=1)
        print(y)
        if abs(abs(y) - abs(x)) < eps:
            found = False
        else:
            x = y
            print(x)
    return y

print(f(0.5)/int(derivative(f, 0.5, dx=1)))

print(newTon())