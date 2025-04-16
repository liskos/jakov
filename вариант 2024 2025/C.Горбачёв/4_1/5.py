def pr(n):
    t = "01234"
    s = ""
    while n > 0:
        s = t[n%5] + s
        n //= 5
    return s

def f(n):
    b = pr(n)
    if n % 2 == 0:
        b = "3" + b + str(n % 5)
    else:
        b = str(n % 4) + b + "4"

    return int(b,5)

print(f(6),f(13))

for i in range(1,16):
    print(f(i))