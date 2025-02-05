def drug(n):
    a = set()
    for i in range(2,int(n**0.5)+1):
        if n % i == 0:
            a.add(n//i)
            a.add(i)
    a.add(1)
    return sum(a)


for i in range(2,30000+1):
    d = drug(i)
    if d > i and drug(d) == i:
        print(i,d)

