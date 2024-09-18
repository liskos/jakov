def sr(n):
    s = ""
    t = "0123456"
    while n > 0:
        s = t[n%7] + s
        n //= 7
    return s

for x in range(1,2030):
    s = (7 ** 91 + 7 ** 160 - x)
    s = sr(s)
    if s.count("0") == 70:
        print(x)


        def tr(n):
            t = "012345"
            s = ""
            while n > 0:
                s = t[n % 6] + s
                n //= 6
            return s


        for x in range(10 ** 3):
            s = (5 ** 2026 + 7 * 5 ** 1013 + 107 - x)
            t = tr(s)
            if t.count('5') - t.count('0') == 28:
                print(x)
                break
