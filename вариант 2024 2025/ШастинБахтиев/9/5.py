def f(n):
    b = oct(n)[2:]
    if n % 2 == 0:
        b = b.replace("1","2").replace("3","2").replace("5","2").replace("7","2")
    else:
        b = "3" + b[1:-1] + "3"
    return int(b,8)

print(f(9),f(12))


b = []
for i in range(1,10000):
    if f(i) < 300:
        b.append(f(i))

print(max(b))