def delitel(n):
    a = set()
    for i in range(1,int(n**0.5)+1):
        if n % i == 0:
            a.add(i)
            a.add(n//i)
    return sorted(a,reverse=True)
d = []
for n in range(573213,575341):
    divs = delitel(n)
    if len(divs) == 4:
        d.append(sum(divs))

for n in range(573213,575341):
    divs = delitel(n)
    if sum(divs) == min(d):
        print(sum(divs),divs)


#574992 967