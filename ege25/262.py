import fnmatch
def delitel(n):
    a = set()
    for i in range(1,int(n**0.5)+1):
        if n % i == 0:
            a.add(i)
            a.add(n//i)
    return a


for i in range(10**9+1,10**11+1):
    if fnmatch.fnmatch(str(i),"1*2*7*04") and len(delitel(i)) == 45:
        divs = delitel(i)
        divs.remove(i)
        print(i,max(delitel(i)))