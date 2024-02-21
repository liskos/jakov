def alg(x):
    a = x % 2
    b = x % 3
    c = x % 5
    a = str(a) + str(b) + str(c)
    return a


f=0
a = []
for i in range(10, 100):
    if alg(i) == '122':
        print(i)
