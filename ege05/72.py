def alg(x):
    a = x//100 + 4
    b = x//10%10 + 8
    c = x%10 + 6
    x = sorted([a,b,c])
    return str(x[2]) + str(x[1]) + str(x[0])





for i in range(100,1000):
    if alg(i) == '13107':
        print(i)
