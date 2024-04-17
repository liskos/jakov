def tr(n):
    t = "01234"
    s = ""
    while n > 0:
        s = t[n % 5] + s
        n //= 5
    return s


s = (5 ** 300 * 15 ** 100) -(25 ** 50 + 125 ** 100)
t = tr(s)
t = t.replace('4',"")
print(sum(map(int,t)),t)
