from functools import cache


@cache
def f(a, b, c=False):
    if a == b:
        return 1
    if a > b:
        return 0
    if a == 23:
        return 0
    if c:
        return f(a + 2, b, False) + f(a * 2, b, False)
    return f(a + 1, b, True) + f(a + 2, b, False) + f(a * 2, b, False)


print(f(3, 11) * f(11, 79))
