def tr(n, i):
    t = "0123456789"
    s = ""
    while n > 0:
        s = t[n % i] + s
        n //= i
    return s
p=0
for i in range(2,11):
    s = sum(map(int,tr(622,i)))
    if s % 2 == 0:
        p+=i
print(p)
