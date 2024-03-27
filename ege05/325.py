def f(n):
    for _ in range(5):
        n = n + int(str(n)[::-1])
        if str(n) == str(n)[::-1]:
            return True
    return False

a = []
for i in range(100,201):
    if (str(i) == str(i)[::-1]) or f(i):
        a.append(i)
print(len(a))
