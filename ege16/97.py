def f(n):
    if n>0 and n % 2 == 0:
        return f(n//2) + 3
    if n > 0 and n % 2 != 0:
        return f(n - 1) + 3
