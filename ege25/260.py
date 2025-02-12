import fnmatch
def delitel(n):
    a = set()
    for i in range(1,int(n**0.5)+1):
        if n % i == 0:
            a.add(i)
            a.add(n//i)
    return a
for i in range(1,10**7+1):
    if fnmatch.fnmatch(str(i),"3*52?") and len(delitel(i)) % 2 != 0:
        divs = delitel(i)
        divs.remove(i)
        print(i,max(delitel(i)))


# 3143529 3143529
# 3175524 3175524
# 3200521 3200521
# 3845521 3845521
# 3908529 3908529