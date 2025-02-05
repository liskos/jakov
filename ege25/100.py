def delitel(n):
    a = set()
    for i in range(1,int(n**0.5)+1):
        if n % i == 0:
            a.add(i)
            a.add(n//i)
    return a

chet = []
nechet = []
for n in range(326496,649633):
    divs = delitel(n)
    for v in divs:
        if v % 2 == 0:
            chet.append(v)
        else:
            nechet.append(v)
    if (chet == nechet) and (len(chet) == 70) and (len(nechet) == 70):
        print(n,min(divs))