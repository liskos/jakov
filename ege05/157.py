def alg(n):
    b = bin(n)[2:]
    b = '0' * (8 - len(b)) + b
    s = ''
    for i in b:
        if i == '1':
            s += '0'
        else:
            s += '1'
    return int(s,2) - n

print(alg(13))
for i in range(0,256):
    if alg(i) == 113:
        print(i)