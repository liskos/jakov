def f(n):
    n = str(n)
    d = 0
    for i in range(len(n)):
        d += int(n[len(n)-1-i]) * (2 ** i)
    return d

def g(h):
    m = 0
    for i in range(223,0,-1):
        b = bin(i)[2:]
        if i % 5 == 0:
            v = '1' + b[-2:]
        else:
            v = bin(i % 5)[2:] + b
        d = f(v)
        if d <= 223:
            m = max(m,d)
        return m

for i in range(2,1000):
    if g(i) <= 223:
        print(f(i))