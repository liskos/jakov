def f(n):
    s1 = 0
    s2 = 0
    for digit in str(n):
        if int(digit) % 2 != 0:
            s1 += int(digit)
    s2 = sum(map(int,str(n)[1::2]))
    return abs(s1 - s2)

print(f(1234))

for i in range(1,100000000):
    if f(i) == 29:
        print(i)