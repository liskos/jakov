def tr(n):
    t = "012"
    s = ""
    while n > 0:
        s = t[n % 3] + s
        n //= 3
    return s

s = 2**5 * 3**25
t = tr(s)
print(t.count('0'),t.count('1'),t.count('2'))