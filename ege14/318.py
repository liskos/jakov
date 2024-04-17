def tr(n):
    t = "0123456789abcdef"
    s = ""
    while n > 0:
        s = t[n % 16] + s
        n //= 16
    return s


s = 16 ** 44 * 16 ** 30 - (32 ** 5 * (8 ** 40 - 8 ** 32)*(16 ** 17 - 32 ** 4))
t = tr(s)
t = t.replace('e',"1")
t = t[:-3]
print(t,t.count('0'))
