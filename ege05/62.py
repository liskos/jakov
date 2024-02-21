def alg(n):
    s1, s2, s3, s4 = str(n)
    a = int(s1) + int(s3)
    b = int(s2) + int(s4)
    a, b = min(a, b),max(a, b),
    return str(a) + str(b)

a = []
for i in range(1000, 9999+1):
    if alg(i) == '1315':
        a.append(i)
print(max(a))
