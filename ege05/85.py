def alg(n):
    s = bin(n)[2:]
    b = s.count('1')
    if b % 2 !=0:
        r = str(s) + "0"
    else:
        r = str(s) + "1"
    if b%2==0:
        r += "1"
    else:
        r += "0"
    return int(r,2)


for i in range(1,1000):
    if alg(i)>54:
        print(i)
        break