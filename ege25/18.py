def delitel(n):
    a = set()
    for i in range(1,int(n**0.5)+1):
        if n % i == 0:
            a.add(i)
            a.add(n//i)
    return sorted(a)

for n in range(143146,143215+1):
    divs = delitel(n)
    if len(divs) == 6:
        print(*divs)

#1 3 9 15907 47721 143163
# 1 2 4 35797 71594 143188
# 1 31 149 961 4619 143189
# 1 2 4 35801 71602 143204
# 1 2 4 35803 71606 143212