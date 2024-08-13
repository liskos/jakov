def f(n):
    if n >= 4938:
        return n + 6
    if n < 4938:
        return n * f(n+5)

print(f(4928)-f(4935))