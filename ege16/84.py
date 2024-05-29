a = set()
def f(n):
    if n < 2:
        return n
    if n >= 2 and n % 2 == 0:
        return f(n//2) + 1
    if n >= 2 and n % 2 != 0:
        return f(3 * n + 1) + 1


for i in range(1,101):
    if f(i) > 100:
        a.add(i)
print(len(a))
