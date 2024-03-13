def f(n):
    b = ''
    c = n
    while c > 0:
        b = str(c % 4) + b
        c = c // 4
    if n % 2 == 0:
        b = '13' + b + '02'
    else:
        b = '2' + b + '11'
    return int(b,4)
print(f(45))


ar = []
for i in range(1,1000):
    if f(i) > 1000:
        ar.append(f(i))
print(sorted(ar)[0])

