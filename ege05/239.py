def g6(h):
    s = '012345'
    r = ''
    while h > 0:
        r = r + s[h % 6]
        h = h // 6
    return r[::-1]

def f(n):
    n = g6(n)
    b = n + n[-1]
    b = int(b,6)
    b = bin(b)[2:]
    b = b + b[-1]
    return int(b,2)
print(f(13))

for i in range(5,1000):
    if f(i) < 344:
        print(f(i))
