def f(n):
    if n <= 1:
        return n
    if n > 1 and n % 3 == 0:
        return n + f(n//3)
    if n > 1 and n % 3 != 0:
        return n + f(n + 3)

print()


