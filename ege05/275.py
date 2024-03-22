def f(n):
    s1 = 0
    s2 = 0
    for digit in str(n):
        if int(digit) % 2 == 0:
            s1 += int(digit)
    s2 = sum(map(int,str(n)[::2]))
    return abs(s1 - s2)

print(g(5))

for i in range(1,10000000):
    if f(i) == 28:
        print(i)