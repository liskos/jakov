
def f(n):
    if n < 3:
        return 3*n % 100
    if n > 2 and n % 2 == 0:
        return (f(n-2) * f(n - 1) - n) % 100
    if n > 2 and n % 2 != 0:
        return (f(n-1) - f(n - 2) + 2 * n) % 100

res = f(30)
print(res)