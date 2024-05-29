def f(n):
    if n <= 1:
        return n
    if n > 1 and n % 3 == 0:
        return n + f(n//3-1)
    if n > 1 and n % 3 != 0:
        return -100000

for i in range(1,100000):
    if f(i) > 1000:
        print(i,f(i))


