def f(n):
    a = (n // 10000) + (n // 10 % 10) + (n % 10)
    b = (n // 1000 % 10) + (n // 10 % 10)
    if a > b:
        n = str(b) + str(a)
    if b > a:
        n = str(a) + str(b)
    return n


b = 0
for i in range(10000,100000):
    if f(i) == '621':
        print(i)
        break
