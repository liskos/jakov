a = set()
def f(n):
    if n == 1:
        return 1
    if n >= 2 and n % 2 == 0:
        return f(n//2) + 1
    if n >= 2 and n % 2 != 0:
        return f(n - 1) + n


for i in range(1,100001):
    if f(i) == 16:
        a.add(i)
print(len(a))
