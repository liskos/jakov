def tr(n):
    s = ""
    t = "012"
    while n > 0:
        s = t[n%3] + s
        n //= 3
    return s


for i in range(1,2031):
    s = 3 ** 100 - i
    s = tr(s)
    if s.count("0") == 5:
        print(i,int(s,3))