def chr(n):
    s = ""
    t = "0123"
    if n == 0:
        return 0
    while n > 0:
        s = t[n%4] + s
        n //= 4
    return s


def f(n):
    b = chr(n)
    if n % 4 == 0:
        b = "2" + b + "03"
    else:
        b = b + chr(n % 4 * 5)

    return int(b,4)

print(f(11))

for i in range(1,10000):
    if f(i) <= 567:
        print(i)