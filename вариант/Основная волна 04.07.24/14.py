def ches(n):
    t = "012345"
    s = ""
    while n > 0:
        s = t[n%6] + s
        n //= 6
    return s
a = []
for x in range(1, 2030+1):
    s = 6 ** 260 + 6 ** 160 + 6 ** 60 - x
    if ches(s).count("0")==202:
        if x == 1944:
            print(x,int(ches(s),6))