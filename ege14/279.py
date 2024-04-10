def tr(n, i):
    t = "0123456789"
    s = ""
    while n > 0:
        s = t[n % i] + s
        n //= i
    return s


def f(t):
    for i in range(len(t)- 1):
        if t[i] >= t[i + 1]:
            return False
    return True
p=0
for i in range(2,11):
    s = tr(123,i)
    if f(s):
        p+=i
print(p)