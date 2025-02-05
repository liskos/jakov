def delitel(n):
    a = set()
    for i in range(1,int(n**0.5)+1):
        if n % i == 0:
            a.add(i)
            a.add(n//i)
    return sorted(a)

for n in range(125873,136763):
    divs = delitel(n)
    if len(divs) == 5:
        print(*divs)

#1 19 361 6859 130321
