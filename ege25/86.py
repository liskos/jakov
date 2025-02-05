def delitel(n):
    a = set()
    for i in range(1,int(n**0.5)+1):
        if n % i == 0:
            a.add(i)
            a.add(n//i)
    return a


k = 0
for n in range(4986,32599+1):
    divs = delitel(n)
    if len(divs) == 4:
        k+=n
print(k)


#124478618
