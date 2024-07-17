def f(a, b, k=0):
    if a == b and k <= 2:
        return 1
    if a > b and k > 2:
        return 0
    if a % 2 != 0:
        return f(a + 2, b) + f(a * 2, b)
    if a % 2 == 0:
        return f(a + 2, b, k) + f(a * 2 + 1, b, k + 1)

print(f(2, 35))