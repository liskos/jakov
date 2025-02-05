def delitel(n):
    a = set()
    for i in range(1,int(n**0.5)+1):
        if n % i == 0:
            a.add(i)
            a.add(n//i)
    return sorted(a,reverse=True)

b = []
for n in range(394480,394541):
    divs = delitel(n)
    b.append(len(divs))

for n in range(394480,394541):
    divs = delitel(n)
    if len(divs) == max(b):
        print(n,len(divs),*divs,)

#1 48 394485 131495
#2 48 394500 197250
#3 48 394506 197253
#4 48 394524 197262