def f(n):
    s1,s2,s3,s4 = str(n)
    if int(s1) % 2 == 0:
        r = int(s1) + int(s3) + abs(int(s2) - int(s4))
    else:
        ar = [s1,s2,s3,s4]
        ar = sorted(ar)
        r = ar[0] + ar[1] + ar[2] + ar[3]
        r = bin(int(r))[2:]
        r = int(r.count('1'))
    return r


n = 0
for i in range(1000,10000):
    if f(i) > 20:
        n += 1
print(n)