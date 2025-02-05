def delitel(n):
    a = set()
    for i in range(1,int(n**0.5)+1):
        if n % i == 0:
            a.add(i)
            a.add(n//i)
    return a


k = 0
for n in range(3661,33625+1):
    divs = delitel(n)
    if len(divs) == 3:
        k+=1
print(k)

#25