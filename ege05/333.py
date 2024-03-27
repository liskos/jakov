def f(n):
    s = ''
    b = n
    k = ''
    while b > 0:
        s += str(b % 3)
        b //= 3
    if n % 3 == 0:
        s += s[-1] + s[-2]
    else:
        a = n % 3 * 5
        while a > 0:
            k += str(a % 3)
            a //= 3
        s += k
    return int(s,3)

print(f(11))
for i in range(1,1000):
    if f(i) > 133:
        print(f(i))