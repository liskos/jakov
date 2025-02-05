def delitel(n):
    a = set()
    for i in range(1,int(n**0.5)+1):
        if n % i == 0:
            a.add(i)
            a.add(n//i)
    return sorted(a)

for n in range(157898,157991):
    divs = delitel(n)
    if len(divs) == 6:
        print(*divs)


# 1 2 281 562 78961 157922
# 1 5 25 6317 31585 157925
# 1 3 9 17551 52653 157959
