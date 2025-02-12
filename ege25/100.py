def delitel(n):
    a = set()
    for i in range(1,int(n**0.5)+1):
        if n % i == 0:
            a.add(i)
            a.add(n//i)
    chet = [x for x in a if x % 2 == 0]
    nechet = [x for x in a if x % 2 != 0]
    minim = [x for x in a if x > 1000]
    if len(chet) >= 70 and (len(nechet) == len(chet)):
        return True,min(minim)
    else:
        return False

for n in range(326496,649633):
    if delitel(n):
        print(n,delitel(n)[1])


# 450450 1001
# 589050 1050
# 630630 1001