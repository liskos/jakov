def f(n):
    n = bin(n)[2:]
    if n.count('1') == n.count('0'):
        n += n[-1]
    elif n.count('1') > n.count('0'):
        n += '0'
    else:
        n += '1'
    if n.count('1') == n.count('0'):
        n += n[-1]
    elif n.count('1') > n.count('0'):
        n += '0'
    else:
        n += '1'
    if n.count('1') == n.count('0'):
        n += n[-1]
    elif n.count('1') > n.count('0'):
        n += '0'
    else:
        n += '1'
    return int(n,2)


for i in range(2,1000):
    if f(i) % 4 == 0:
        print(i)
