import sys

sys.setrecursionlimit(100000)


def g(n, d):
    if n % d == 0:
        return g(n // d, d)
    return n


def f(n, d):
    if n == 1:
        return
    if d * d > n:
        print(n)
        return
    if n % d == 0:
        print(d)
        f(g(n, d), d + 1)
    else:
        f(n, d + 1)


n = int(input())
f(n, 2)
