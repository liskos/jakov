def f(a,b,c,c1,ff):
    if c>0 and c1>0 and (a+c+c1)%11==0:ff = 1

    if a > b:return 0
    if a == b:return ff == 1
    if a<b:return f(a+2,b,a,c,ff)+f(a*3,b,a,c,ff)+f(a*4,b,a,c,ff)
print(f(1,600,0,0,0))