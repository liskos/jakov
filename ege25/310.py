import fnmatch
def delitel(n):
    a = set()
    for i in range(1,int(n**0.5)+1):
        if n % i == 0:
            a.add(i)
            a.add(n//i)
    return sum(a)
for i in range(500001,10000000):
    if fnmatch.fnmatch(str(delitel(i)),"*7?"):
            print(i,delitel(i))


# 500001 666672
# 500048 968874
# 500069 500070
# 500079 666776
# 500114 750174