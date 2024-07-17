def f(a,b,k):
    if a % 2 != 0:
        k+=1
    if a > b:return 0
    if a == b: return k<=7
    if a < b: return f(a+2,b,k)+f(a*2,b,k)+f(a*3,b,k)
print(f(1,214,0))