def chr(n):
    t = '0123'
    s = ''
    while n > 0:
        s = t[n%4] + s
        n //= 4
    return s


for x in range(32):
    s1 = 1 * 32 ** 4 + 7 * 32 ** 3 + 9 * 32 ** 2 + x * 32 ** 1 + 9
    s2 = 7 * 128 ** 3 + x * 128 ** 2 + 9 * 128 ** 1 + 3
    a = chr(s1+s2)
    print(x,a,a.count('0'))
    print(sum(map(int,a)))
