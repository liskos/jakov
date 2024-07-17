def f(a,b,k):
    if a % 6 == 0:
        k+=1
    if a > b:return 0
    if a == b: return k<=4
    if a < b: return f(a+2,b,k)+f(a*2,b,k)+f(a*3,b,k)
print(f(1,300,0))