def chr(n):
    t = "0123"
    s = ""
    while n > 0:
        s = t[n%4]+s
        n //= 4
    return s

def f(n):
    b = chr(n)
    if sum(map(int,b))% 2 == 0:
        b = "31" + b + "02"
    else:
        b = "1" + b + chr((int(b)% 3)*7)
    return int(b,4)


print(f(11),f(12))