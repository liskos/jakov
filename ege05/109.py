def alg(x):
    a = x % 7
    b = x % 2
    c = x % 5
    a = str(a) + str(b) + str(c)
    return a


f=0
a = []
for i in range(10, 100):
    if alg(i) == '312':
        print(i)
