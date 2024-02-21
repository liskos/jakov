def f(x):
    r = 1
    a = (x//100) * (x//10%10)
    b = (x//10%10) * x%10
    a,b = max(a,b),min(a,b)
    d = str(a) + str(b)
    return d


for i in range(100,1001):
    if f(i)=='123':
        print(i)
        break