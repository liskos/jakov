import fnmatch
def delitel(n):
    a = set()
    for i in range(1,int(n**0.5)+1):
        if n % i == 0:
            a.add(i)
            a.add(n//i)
    return a
for i in reversed(range(1,10**7+1)):
    if fnmatch.fnmatch(str(i),"9?*55*7"):
        print(i,sum(delitel(i))%21)


#9995597 18
#9996557 12
#9997557 12
#9998557 17
#9999557 0
