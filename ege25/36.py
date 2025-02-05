def delitel(n):
    a = set()
    for i in range(1,int(n**0.5)+1):
        if n % i == 0:
            a.add(i)
            a.add(n//i)
    return sorted(a,reverse=True)

b = []
for n in range(194441,196501):
    divs = delitel(n)
    if len(divs) % 2 != 0:
        print(n,len(divs),int(n**0.5),divs)


#1 194481 25 441
#2 195364 27 442
#3 196249 3 443