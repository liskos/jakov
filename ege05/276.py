def f(n):
    s1 = 0
    s2 = 0
    for digit in str(n):
        if int(digit) % 2 == 0:
            s1 += int(digit)
    for digit in str(n):
        if int(digit) % 2 != 0:
            s2 += int(digit)
    return abs(s1 - s2)

print(f(1234))

for i in range(1,1000):
    if f(i) == 27:
        print(i)