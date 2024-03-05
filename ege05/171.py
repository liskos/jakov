def alg(n):
    n = bin(n)[2:]
    b = '0' * (8 - len(n)) + n
    b = b[0] + b[1] + b[-2] + b[-1]
    return int(b,2)


for i in range(130,256):
    if alg(i) == 10 :
         print(i)


