def sr(n):
    t = "0123456"
    s = ""
    while n > 0:
        s = t[n%7]+s
        n //= 7
    return s

s = 5 * 343 ** 2031 + 4 * 49 ** 2142 - 3 * 7 ** 111 + 7 ** 222
b = sr(s)
print(sum(map(int,b)))
