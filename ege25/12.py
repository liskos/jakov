def delitel(n):
    a = set()
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            a.add(i)
            a.add(n // i)
    return sorted(a)


for n in range(193136, 193223 + 1):
    divs = delitel(n)
    if len(divs) == 6:
        print(*divs)

#1 5 25 7727 38635 193175
# 1 2 4 48299 96598 193196
# 1 3 9 21467 64401 193203
# 1 7 49 3943 27601 193207