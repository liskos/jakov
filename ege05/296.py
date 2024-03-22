def f(n):
    n = str(n)
    s1 = n[::2]
    s1 = [(int(i)*2)%10 +(int(i)*2)//10 for i in s1]
    s1 = sum(s1)
    s2 = n[1::2]
    s2 = sum(map(int,s2))
    return (s1 + s2) % 10 == 0


for i in range(1234567891011121,10**18):
    if f(i):
        print(i % 100000000)
        break
