def tr(n, i):
    t = '0123456789'
    s = ''
    while n > 0:
        s = t[n % i] + s
        n //= i
    return s


for n in range(2,11):
    s = n ** 25 - 2 * n ** 13 + 10
    t = tr(s,n)
    if (sum(map(int,t))) == 75 :
        print(n)