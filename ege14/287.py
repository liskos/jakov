for x in range(1, 10000):
    s = bin(4 ** 1014 - 2 ** x + 12)[2:]
    if s.count('0') == 2000:
        print(x)
        break
