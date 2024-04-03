def tr(n):
    t = "0123456"
    s = ""
    while n > 0:
        s = t[n % 7] + s
        n //= 7
    return s

s = 3**3 * 7**69 - 70
t = tr(s)
print(t.count('0'),t.count('1'),t.count('2'),t.count('3'),t.count('4'),t.count('5'),t.count('6'))