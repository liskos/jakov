def f(n):
    n = bin(n)[2:]
    if n.count('1') % 2 == 0:
        a = '0'
    else:
        a = '1'
    r = n + a
    if r.count('1') % 2 == 0:
        b = '0'
    else:
        b = '1'
    r+=b
    return int(r,2)



k = 0
for i in range(16,33):
    if (16<= f(i) <= 32) == False:
        k += 1
print(k)