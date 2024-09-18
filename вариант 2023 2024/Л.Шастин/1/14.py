s = set()
for x in range(2,67):
    for y in range(0,x):
        s1 = 7 * 67 ** 4 + 3 * 67 ** 3 + x * 67 ** 2 + 1 * 67 + y
        s2 = 4 * x ** 3 + 9 * x ** 2 + y * x + 6
        s.add(s1 + s2)
print(len(s))