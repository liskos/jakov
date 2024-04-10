def tr(n):
    t = "0123456789abcdefghjklmnop"
    s = ""
    while n > 0:
        s = t[n % 25] + s
        n //= 25
    return s


s =
t = tr(s)
print(t.count('0'),t)
