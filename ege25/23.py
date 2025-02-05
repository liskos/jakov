def delitel(n):
    a = set()
    for i in range(1,int(n**0.5)+1):
        if n % i == 0 and i % 2 != 0:
            a.add(i)
            a.add(n//i)
    return sorted(a,reverse=True)


for n in range(190061,190081):
    divs = delitel(n)
    if len(divs) == 4:
        print(*divs)

# 190061 6131 31 1
# 190064 27152 7 1
# 190067 2677 71 1
# 190072 8264 23 1
# 190073 14621 13 1
# 190078 27154 7 1
# 190079 2837 67 1