def f(a,b, k):
    if a == b:
        return 1
    if k == 0:
        return 0
    if a > b:
        return 0
    return f(a+1,b,k-1)+f(a*2,b,k-1)+f(a+(a%4),b,k-1)

m = 0
for i in range(1,81):
    if f(i,80,5):
        m+=1

print(m)