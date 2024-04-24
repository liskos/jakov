def tr(n):
    t ='0123456789abcdefghijklmno'
    s = ''
    while n > 0:
        s = t[n % 25] + s
        n //= 25
    return s

s = 3 * 3125 ** 9 + 2 * 625 ** 8 - 4 * 625 ** 7 + 3 * 125 ** 6 - 2 * 25 ** 5 - 2024
s = tr(s)
print(s,s.count('0'))