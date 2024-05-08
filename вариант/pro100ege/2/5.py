def tr(n):
    t = '012'
    s = ""
    while n > 0:
        s = t[n%3] + s
        n //= 3
    return s

def f(n):
    b = tr(n)
    if n % 2 == 0:
        b = "1" + b + "00"
        return int(b,3)
    else:
        b += str(tr((sum(map(int,b)))))
        return int(b,3)
print(f(4))
print(f(7))


for i in range(1,100):
    if f(i) > 168:
        print(i)