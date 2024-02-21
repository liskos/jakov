def f(x):
    s1, s2, s3, s4 = str(x)
    a = sorted([int(s1) + int(s2), int(s2) + int(s3), int(s3) + int(s4)])
    return str(a[2]) + str(a[1])


for i in range(1000, 10000):
    if f(i) == '1713':
        print(i)
        break
