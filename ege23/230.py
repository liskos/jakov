def f(a, b, c=0, v=0, n=0):
    if a == b:
        return 1
    if a > b:
        return 0
    if c == 1:
        return f(a * 2, b, c - 1, v + 1, n) + f(a * 2, b, c - 1, v, n + 1)
    if v == 1:
        return f(a + 1, b, c + 1, v - 1, n) + f(a * 2, b, c, v - 1, n + 1)
    if n == 1:
        return f(a + 1, b, c + 1, v, n - 1) + f(a * 2, b, c, v + 1, n - 1)
    if c == 1 and v == 1:
        return f(a * 2, b, c - 1, v - 1, n + 1)
    if c == 1 and n == 1:
        return f(a * 2, b, c - 1, v + 1, n - 1)
    if c == 1 and n == 1 and v == 1:
        return 0
    return f(a + 1, b, c + 1, v, n) + f(a * 2, b, c, v + 1, n) + f(a * 2, b, c, v, n + 1)

print(f(5001, 45789))