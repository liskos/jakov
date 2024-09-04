a = []
for x in range(2030):
    s = 6 * 2030 + 6 * 100 - x
    s = int(s,6)
    a.append(s.count("0"))