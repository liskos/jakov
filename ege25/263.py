import fnmatch
def delitel(n):
    a = set()
    for i in range(1,int(n**0.5)+1):
        if n % i == 0:
            a.add(i)
            a.add(n//i)
    return a


for i in range(1,10**9+1):
    if fnmatch.fnmatch(str(i),"15*3*09"):
        if len(delitel(i)) == 9:
            divs = delitel(i)
            divs.remove(i)
            print(i,max(divs))