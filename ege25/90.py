def delitel(n):
    a = set()
    for i in range(1,int(n**0.5)+1):
        if n % i == 0:
            a.add(i)
            a.add(n//i)
    return a


a = []
k = 0
for n in range(3594,21891+1):
    divs = delitel(n)
    if len(divs) == 4:
        a.append(n)

print(max(a))


#21891