import sys,func
sys.stdin=open("27_A_17834.txt")
cl_a = []
cl_b = []

for _ in range(995):
    x,y = map(float,input().split())
    if x < 6 :
        cl_a.append([x,y])
    else:
        cl_b.append([x,y])

xa,ya = func.func(cl_a)
xb,yb = func.func(cl_b)
print((xa+xb)/2*100,(ya + yb)/2*100)
#597 432
