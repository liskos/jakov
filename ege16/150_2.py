def f(n):
    if n in a:
        return a[n]
    if n <= 3:
        a[n] = n - 1
        return n - 1
    if n > 3 and n % 2 == 0:
        a[n] = f(n - 2) + n // 2 - f(n - 4)
        return a[n]
    if n > 3 and n % 2 != 0:
        a[n] = f(n - 1) * n + f(n - 2)
        return a[n]


a = dict()
for i in range(1, 5000):
    f(i)
print(f(4952) + 2 * f(4958) + f(4964))
