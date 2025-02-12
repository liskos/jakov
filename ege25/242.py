import fnmatch
def delitel(n):
    a = set()
    for i in range(1,int(n**0.5)+1):
        if n % i == 0:
            a.add(i)
            a.add(n//i)
    x = [x for x in a if x % 2 != 0]
    return x
for i in reversed(range(1,10**7+1)):
    if fnmatch.fnmatch(str(i),"14?4*"):
        if i % 217 == 0:
            print(i,sum(delitel(i)))

# 1494913 1785088
# 1494696 306432
# 1494479 1806336
# 1494262 964608
# 1494045 3345408
# 1484931 2336768
# 1484714 958464