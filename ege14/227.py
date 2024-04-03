def tr(n):
    t = '0123'
    s = ""
    while n > 0:
        s = t[n % 4] + s
        n //= 4
    return s

s = ((44 + 4 ** 50) * 4 ** 25 + 44) * 4 ** 12 + 44
t = tr(s)
print(t.count('0'),t.count('1'),t.count('2'),t.count('3'))