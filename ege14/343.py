def tr(n):
    k = 0
    while n > 0:
        if n%64==0:
            k += 1
        n = n//64
    return k


s = 7 * 512 ** 3200 + 6 * 256 ** 3100 - 5 * 64 ** 3000 - 4 * 8 ** 2900 - 1542
t = tr(s)
print(t)
