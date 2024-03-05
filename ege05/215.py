def f(n):
    s1,s2,s3 = str(n)
    a = s1 + s2
    b = s2 + s3
    c = s1 + s3
    d = s3 + s1
    e = s2 + s1
    v = s3 + s2
    a,b = max(a,b,c,d,e,v),min(a,b,c,d,e,v)
    return int(a) - int(b)


print(f(351))

for i in range(100,1000):
    if f(i) == 35:
        print(i)