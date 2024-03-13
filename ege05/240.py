def g(h):
    h = str(h)
    k = ''
    for n in h:
        t = bin(int(n))[2:]
        k += '0' * (4 - len(t)) + t
    k = k.replace('1','8')
    k = k.replace('0','1')
    k = k.replace('8','0')
    return int(k,2)


print(g(13))
for i in range(1,1000):
    if g(i) == 151:
        print(i)