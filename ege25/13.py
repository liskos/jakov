def delitel(n):
    a = set()
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            a.add(i)
            a.add(n // i)
    return sorted(a)


for n in range(100812, 100923 + 1):
    divs = delitel(n)
    if len(divs) == 6:
        print(*divs)

# 1 17 289 349 5933 100861
# 1 2 4 25219 50438 100876
# 1 2 4 25229 50458 100916
# 1 3 9 11213 33639 100917