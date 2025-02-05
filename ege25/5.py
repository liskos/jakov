def delitel(n):
    a = set()
    for i in range(1,int(n**0.5)+1):
        if n % i == 0:
            a.add(i)
            a.add(n//i)
    return sorted(a)

for n in range(150750,150765):
    divs = delitel(n)
    if len(divs) == 4:
        print(*divs)

# 1 233 647 150751
# 1 2 75377 150754
# 1 41 3677 150757
# 1 13 11597 150761
# 1 107 1409 150763

