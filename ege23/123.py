def f(a,b,k):
    if a == b:
        return 1
    if k <= 5:
        return 0
    return f(a+1,b,1)+f(a*2,b,1)+f(a+(a%4),b,1)

m = 0
for i in range(1,1000):
    if f(i,80,0):
        m+=1

print(m)