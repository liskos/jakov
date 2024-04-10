def tr(n,i):
    t = '0123456789'
    r = ''
    while n > 0 :
        r = t[n % i] + r
        n //= i
    return r


for i in range(2,11):
    t = tr(78,i)
    print(t,i)