def alg(x):
    return str(x % 4) + str(x % 2) + str(x % 5)


for i in range(10, 100):
    if alg(i) == '202':
        print(i, alg(i))

