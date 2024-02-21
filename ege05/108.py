def alg(x):
    a = x % 4
    b = x % 3
    c = x % 2
    a = str(a) + str(b) + str(c)
    return a


f=0
a = []
for i in range(10, 100):
    if alg(i) == '200':
        print(i)
