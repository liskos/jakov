def f(n):
    if n == 6:
        return 100000000
    if n > 1000000:
            return 1000000
    if n <= 5:
        return n
    if n > 5 and n % 5 == 0:
        return n + f(n//5+1)
    if n > 5 and n % 5 != 0:
        return n+f(n+6)

for i in range(1,1000):
    if f(i) > 1000 and f(i) < 10000:
        print(i,f(i))



