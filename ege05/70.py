def alg(n):
    s1, s2, s3 = str(n)
    a = int(s1) + int(s2)
    b = int(s2) + int(s3)
    a, b = max(a, b),min(a, b)
    return str(a) + str(b)


f=0
a = []
for i in range(100, 999+1):
    if alg(i) == '43':
        print(i)
        break


