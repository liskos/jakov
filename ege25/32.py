def delitel(n):
    a = set()
    for i in range(1,int(n**0.5)+1):
        if n % i == 0:
            a.add(i)
            a.add(n//i)
    return sorted(a,reverse=True)

b = []
for n in range(394441,394506):
    divs = delitel(n)
    b.append(len(divs))

for n in range(394441,394506):
    divs = delitel(n)
    if len(divs) == max(b):
        print(*divs,
              "\n",len(divs))
        break

#48 394450 197225