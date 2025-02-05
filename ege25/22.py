def delitel(n):
    a = set()
    for i in range(1,int(n**0.5)+1):
        if n % i == 0 and i % 2 == 0:
            a.add(i)
            a.add(n//i)
    return sorted(a,reverse=True)


for n in range(190201,190281):
    divs = delitel(n)
    if len(divs) == 4:
        print(*divs)

# 95117 8647 22 2
# 95119 1303 146 2
# 95126 47563 4 2
# 95137 13591 14 2
# 95138 47569 4 2

