def delitel(n):
    a = set()
    for i in range(1,int(n**0.5)+1):
        if n % i == 0:
            a.add(i)
            a.add(n//i)
    return sorted(a)

for n in range(135743,135789+1):
    divs = delitel(n)
    if len(divs) == 6:
        print(*divs)


#1 3 9 15083 45249 135747
# 1 2 4 33937 67874 135748
# 1 2 4 33941 67882 135764
# 1 5 25 5431 27155 135775