def alg(n):
    s = bin(n)[2:]
    if s.count('1') % 2 == 0:
        s += "1"
    else:
        s += "0"
    if s.count('1') % 2 == 0:
        s += "1"
    else:
        s += "0"
    return int(s, 2)


for i in range(1, 1000):
    if alg(i) > 184:
        print(i, alg(i))
        break
