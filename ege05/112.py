def f(x):
    a = (x // 100) * (x // 10 % 10)
    b = (x // 10 % 10) * (x % 10)
    a, b = max(a, b), min(a, b)
    d = str(a) + str(b)
    return d


print(f(179))
for i in range(100, 1000):
    if f(i) == '123':
        print(i)
        break
