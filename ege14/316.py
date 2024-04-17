def tr(n):
    t = "01234567"
    s = ""
    while n > 0:
        s = t[n % 8] + s
        n //= 8
    return s


s = 8 ** 20 + ((8 ** 22 - 8 ** 17) * (8 ** 13 + 8 ** 16))
t = tr(s)
t = t.replace('7',"0")
t = t[:-3]
print(sum(map(int,t)),t)
