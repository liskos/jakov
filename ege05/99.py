def f(n):
    s1, s2, s3, s4, s5 = str(n)
    a = int(s1) + int(s3) + int(s5)
    b = int(s2) + int(s4)
    a, b = max(a, b), min(a, b)
    return str(b) + str(a)


print(f(63179))
b = 0
for i in range(10000, 100000):
    if f(i) == '621':
        print(i)
        break
