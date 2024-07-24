def f(a, b):
    if a < b:
        return 0
    if a == b:
        return 1
    m = 10
    z = a
    while z > 0:
        if 0 < z % 10 < m:
            m = z % 10
        z //= 10
    k = f(a - 2, b) + f(a - m, b)
    if a % 4 != 0:
        k += f(a - a % 4, b)
    return k
print(f(96, 64) * f(64, 60))