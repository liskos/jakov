def g(h):
    b = ''
    while h > 0:
        b = str(h % 4) + b
        h = h // 4
    return b
def f(n):
    n = g(n)
    b = int(n) % 2
    c = int(n) % 3
    n = str(b) + n + str(c)
    return int(n,4)

print(f(23))


for i in range(1,1000):
    if f(i)< 100:
        print(f(i))