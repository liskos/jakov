def alg(n):
    n = bin(n)[2:]
    if int(n) % 2 == 0:
        n += "00"
    else:
        n += '11'
    return int(n,2)


for i in range(1,1000):
    if alg(i) > 115:
        print(i)
        break