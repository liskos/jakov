import fnmatch
def delitel(n):
    a = set()
    for i in range(1,int(n**0.5)+1):
        if n % i == 0:
            a.add(i)
            a.add(n//i)
    return a



p = 0
for i in range(1,(17*(10**6))+1):
    if fnmatch.fnmatch(str(i),"*1?*?68*") and i % 161 == 0 and ((p == 0) or (p % 500 == 1)):
        p += 1
        print(i,i//161,p)


#14168 88 1
