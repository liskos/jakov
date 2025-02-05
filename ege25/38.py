def delitel(n):
    a = set()
    for i in range(1,int(n**0.5)+1):
        if n % i == 0:
            a.add(i)
            a.add(n//i)
    return sorted(a,reverse=True)
d = []
for n in range(268220,270336):
    divs = delitel(n)
    if len(divs) < 5:
        d.append(sum(divs))
b = 0
for n in range(268220,270336):
    divs = delitel(n)
    if sum(divs) == max(d):
        b += 1
        print(sum(divs),len(divs),*divs)


#405456 4 270302 135151 2 1