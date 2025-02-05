def delitel(n):
    a = set()
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            a.add(i)
            a.add(n // i)
    return sorted(a)


for n in range(164700, 164752 + 1):
    divs = delitel(n)
    if len(divs) == 6:
        print(*divs)

#1 2 4 41177 82354 164708
# 1 3 9 18301 54903 164709
# 1 2 4 41179 82358 164716
# 1 2 4 41183 82366 164732