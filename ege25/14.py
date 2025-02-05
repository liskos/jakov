def delitel(n):
    a = set()
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            a.add(i)
            a.add(n // i)
    return sorted(a)


for n in range(177399, 177453 + 1):
    divs = delitel(n)
    if len(divs) == 6:
        print(*divs)


#1 2 4 44351 88702 177404
# 1 11 127 1397 16129 177419
# 1 2 4 44357 88714 177428
# 1 29 211 841 6119 177451
# 1 3 9 19717 59151 177453