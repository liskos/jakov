from string

def chr(n):
    t = "0123"
    s = ""
    if n == 0:
        return "0"
    while n > 0:
        s = t[n%4]+s
        n //= 4

    return s

def f(n):
    b = chr(n)
    if sum(map(int,b))% 2 == 0:
        b = "31" + b + "02"
    else:

        b = "1" + b + chr((n % 3)*7)
    return int(b,4)

print(f(11),f(12))
for i in range(1,100000):
    if f(i) < 4528:
        print(i)