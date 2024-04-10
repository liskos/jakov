def tr(n,i):
    t = '0123456789'
    s = ''
    while n > 0:
        s = t[n % i] + s
        n //= i
    return s

for n in range(2,11):
    t = tr(2345,n)
    print(sum(map(int,t)),n)

