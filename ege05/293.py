def f(n):
    p1 = 1
    p2 = 1
    for i in str(n):
        if int(i) == 0:
            continue
        elif int(i) % 2 == 0:
            p1 = int(i) * p1
        else:
            p2 = int(i) * p2
    return p1,p2

n = 120
for m in range(1,1000):
    n1,n2 = f(n)
    m1,m2 = f(m)
    if abs(n1 * m1 - m2 * n2) == 29:
        print(m)
        break