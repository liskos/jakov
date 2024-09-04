def ches(n):
    k = 0
    while n > 0:
        if n % 6 == 0:
            k += 1
        n //= 6
    return k
a = []
for x in range(1, 2030+1):
    s = 6 ** 2030 + 6 ** 100 - x
    a.append(ches(s))
print(max(a))