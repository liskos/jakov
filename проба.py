def f(n):
    return (n + 1) * (n + 1)


def g(n):
    return n * n


def h(a):
    i = 1
    while f(i) < g(i) + k:
        i += 1
    return i


m = 0
for x in range(1, 1000000):
    if h(x) == 14:
        m = x
print(m)

