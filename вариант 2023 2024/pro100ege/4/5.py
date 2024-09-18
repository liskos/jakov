def chr(n):
    t = '0123'
    s = ''
    while n > 0:
        s = t[n%4] + s
        n //= 4
    return s

def f(n):
    b = chr(n)
    if len(b) % 2 == 0:
        b = b[:len(b)//2] + "0" + b[len(b)//2:]
    return int(b)


print(f(6),f(21))

for i in range(1,1000):
    if f(i) <= 180:
        print(i)