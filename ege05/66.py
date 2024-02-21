def alg(n):
    s1, s2, s3 = str(n)
    a = int(s1) + int(s2)
    b = int(s2) + int(s3)
    a, b = max(a, b),min(a, b)
    return str(a) + str(b)

a = []
for i in range(100, 9999+1):
    if alg(i) == '1412':
        print(i)
        break

