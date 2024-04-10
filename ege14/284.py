def tr(n, i):
    t = "0123456789"
    s = ""
    while n > 0:
        s = t[n % i] + s
        n //= i
    return s

def f(t):
    for i in range(len(t) - 2):
        if int(t[i + 1]) - int(t[i]) != int(t[i + 2]) - int(t[i + 1]):
            return False
    for i in range(len(t) - 1):
        if t[i + 1] >= t[i]:
            return False
    return True
p=0
for i in range(2,11):
    s = tr(210,i)
    if f(s):
        p += i
print(p)
