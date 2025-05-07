def semb(n):
    s = ""
    t = "0123456"
    while n > 0:
        s = t[n%7] + s
        n //= 7
    return s


for x in range(1,2301):
    s = 7 ** 350 + 7 ** 150 - x
    if semb(s).count("0") == 200:
        print(x)
