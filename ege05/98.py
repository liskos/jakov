def f(n):
    a = (n // 100) * (n // 10 % 10)
    b = (n // 10 % 10) * (n % 10)
    if a > b:
        n = str(b) + str(a)
    if b > a:
        n = str(a) + str(b)
    return n


b = 0
for i in range(100,1000):
    if f(i) == '621':
        b = i
print(b)
