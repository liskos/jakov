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


def algor(n):
    """напишите программу автомата сюда"""
    b = bin(n)[2:]
    sum_digit = 0
    for sym in b:
        sum_digit += int(sym)
    b = b + str(sum_digit % 2)
    v = 0
    for sym in str(b):
        v += int(sym)
    b = b + str(v % 2)
    r = int(b, 2)
    return r


print(algor(int(input())))


