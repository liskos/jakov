def f(n):
    s1,s2,s3 = str(n)
    a = int(s1) * int(s2)
    b = int(s2) * int(s3)
    a,b = min(a,b),max(a,b)
    return int(str(a)+str(b))


for i in range(100,1000):
    if f(i) == 621:
        print(i)
