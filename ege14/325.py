def tr(n):
    t = "0123456789abcde"
    s = ""
    while n > 0:
        s = t[n % 15] + s
        n //= 15
    return s


s = 11*15**65 + 18*15**38 - 14* 15**17 + 19*15**11 + 18338
print(len(set(tr(s))))
