def g(h):
    h = oct(h)[2:]
    return h
def f(n):
    j = g(n)
    if sum(map(int,str(n))) % 2 == 0:
        j += str(n % 3)
    else:
        m = max(int(d) for d in j)
        j = str(m) + j
    return int(j,8)

print(f(5))
for i in range(1,10000):
    if f(i) >= 127:
        print(i)