
def f(a, b, k=0):
    if a == b and k <= 5:
        return 1
    if a > b:
        return 0
    if a % 2 != 0:
        return f(a + 3, b) + f(a * 2, b)
    if a % 2 == 0:
        return f(a + 3, b, k) + f(a * 2 + 1, b, k + 1)

print(f(1, 76))