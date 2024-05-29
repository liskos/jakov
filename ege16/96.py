def f(n):
    if n < 10:
        return n
    if n >= 10:
        return n % 10 + f(n // 10)
def g(n):
    if n < 10 :
        return n
    if n >= 10:
        return g(f(n))

print(f(12345678987654321))


