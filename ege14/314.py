def tr(n):
    t = "0123456"
    s = ""
    while n > 0:
        s = t[n % 7] + s
        n //= 7
    return s


s = (7 ** 160 * 7 ** 90) - (14 ** 150 + 2 ** 13)
t = tr(s)
t = t.replace('6',"")
print(sum(map(int,t)),t)
