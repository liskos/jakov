def f(n):
    b = bin(n)[2:]
    b = b.replace("1","8")
    b = b.replace("0","1")
    b = b.replace("8","0")
    if n % 2 == 0:
        b += "10"
    else:
        b += "11"
    return int(b,2)

a = []
for i in range(1,1000):
    if f(i) > 125:
        a.append(f(i))
print(min(a))