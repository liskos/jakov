def dev(n):
    t = "012345678"
    s = ""
    while n > 0:
        s = t[n%9] + s
        n //= 9
    return s


s = 2 * 729 ** 333 + 2 * 243 ** 334 - 81 ** 335 + 2 * 27 ** 336 - 2 * 9 ** 337 - 338
s = dev(s)
print(len(s.replace("0","")))