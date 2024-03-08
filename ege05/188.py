def f(n):
    b = bin(n)[2:]
    b = '0' * (8 - len(b)) + b
    i = b.rfind('1')
    s1 = b[:i]
    s2 = b[i:]
    s1 = s1.replace('0', '8')
    s1 = s1.replace('1', '0')
    s1 = s1.replace('8', '1')
    s = s1 + s2
    return int(s, 2)


print(f(171))