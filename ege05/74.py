def alg(x):
    a = x//100 + 7
    b = x//10%10 + 1
    c = x%10 + 4
    x = sorted([a,b,c])
    return str(x[0]) + str(x[1]) + str(x[2])





for i in range(100,1000):
    if alg(i) == '91012':
        print(i)
