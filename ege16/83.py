def f(n):
    if n > 1000000:
            return 1000000
    if n <= 5:
        return n
    if n > 5 and n % 8 == 0:
        return n + f(n//2-3)
    if n > 5 and n % 8 != 0:
        if n % 4 == 0:
            return n+f(n+4)
        else:
            return 1000000
for i in range(1,1000):
    if f(i) < 1000000:
        print(i,f(i))


