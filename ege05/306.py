def f(n):
    n = bin(n)[2:]
    if n.count('1') + n.count('0') % 2 == 0:
        n = n + '10'
    else:
        n = '11' + n
    return int(n,2)

n = 0
for i in range(100,201):
    if f(i) % 2 == 0:
        n+=1
print(n)