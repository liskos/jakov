def tr(n, i):
    t = "0123456789"
    s = ""
    while n > 0:
        s = t[n % i] + s
        n //= i
    return s


p=0
for i in range(2,11):
    s = tr(437,i)
    if sum(map(int,s)):
        p += i
print(p)
