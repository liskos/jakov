def f(n):
    n = str(n)
    s1 = n[::2]
    s1 = [(int(i)*2)%10 +(int(i)*2)//10 for i in s1]
    s1 = sum(s1)
    s2 = n[1::2]
    s2 = sum(map(int,s2))
    return s1 + s2


for i in range(10**15,10**18):
    if f(i) == 30:
        print(i % 100000000)
        break
