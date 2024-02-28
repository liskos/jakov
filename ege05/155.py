def alg(n):
    n = bin(n)[2:]
    if int(n) % 2 == 0:
        n = n + '01'
    else:
        n = n + '10'
    return int(n,2)


for i in range(1,1000):
    if alg(i) > 97:
        print(i)
        break