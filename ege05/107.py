def alg(x):
    a = x % 4
    b = x % 2
    c = x % 3
    a = str(a) + str(b) + str(c)
    return a


f=0
a = []
for i in range(10, 100):
    if alg(i) == '201':
        print(i)
