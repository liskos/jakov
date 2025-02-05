def delitel(n):
    a = set()
    for i in range(1,int(n**0.5)+1):
        if n % i == 0:
            a.add(i)
            a.add(n//i)
    return sorted(a,reverse=True)

b = 0
for n in range(499,502,2):
    divs = delitel(n**2)
    if len(divs) % 2 != 0:
        b += 1
        print(b,n**2,len(divs),int(n**0.5),divs)


#1 249001 3 499
#2 250000 35 500
#3 251001 9 501
