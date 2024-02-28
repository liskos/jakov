def alg(n):
    s = bin(n)[2:]
    if s.count('1') % 2 == 0:
        s += "0"
    else:
        s += "1"
    if s.count('1') % 2 == 0:
        s += "0"
    else:
        s += "1"
    return int(s, 2)


for i in range(1, 1000):
    if alg(i) > 121:
        print(i, alg(i))
        break
