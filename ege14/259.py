def tr(n,i):
    t = '0123456789'
    r = ''
    while n > 0 :
        r = t[n % i] + r
        n //= i
    return r

def f(s):
    s =str(s)
    for i in "02468":
        s = s.replace(i,'*')
    for d in '13579':
        s = s.replace(d,'#')
    return ("**" not in s) and ("##" not in s)


a = []
for i in range(2,11):
    t = tr(78,i)
    if f(t):
        a.append(i)
print(sum(a))