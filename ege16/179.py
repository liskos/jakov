def f(n):
    if n < 2:
        return n
    if n >= 2:
        return n % 2 + 10 * f(n//2)

print(f(100000100001000100101))