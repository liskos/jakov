def f(n):
    if n > 1000000:
        return n
    if n <= 1000000:
        return 3 * n + f(5 * n)

def g(n):
    return f(n)/n