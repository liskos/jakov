def delitel(n):
    a = set()
    for i in range(1,int(n**0.5)+1):
        if n % i == 0:
            a.add(i)
            a.add(n//i)
    return sorted(a)

for n in range(180131,180180):
    divs = delitel(n)
    if len(divs) == 6:
        print(*divs)


#1 19 361 499 9481 180139
# 1 11 121 1489 16379 180169
# 1 7 49 3677 25739 180173
# 1 5 25 7207 36035 180175