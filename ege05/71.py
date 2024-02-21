def alg(x):
    a = x//100 + 6
    b = x//10%10 + 9
    c = x%10 + 4
    x = sorted([a,b,c])
    return str(x[2]) + str(x[1]) + str(x[0])





for i in range(100,1000):
    if alg(i) == '11108':
        print(i)
