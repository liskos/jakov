def alg(n):
    n = bin(n)[2:]
    b = '0' * (8 - len(n)) + n
    b = b[:7]
    b = b[::-1]
    return int(b,2)


for i in range(100):
    if alg(i) == i :
         print(i)


