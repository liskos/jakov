def tr(n):
    t = '01234567'
    s = ''
    while n > 0:
        s = t[n % 8] + s
        n //= 8
    return s
s = 2 ** 102 + 2 ** 100 + 2 ** 85 + 2 ** 17
t = tr(s)
print(t.count('1'),t.count('2'),t.count('3'),t.count('4'),t.count('5'),t.count('6'),t.count('7'))
