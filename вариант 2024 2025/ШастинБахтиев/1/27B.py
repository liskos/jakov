import sys,func
sys.stdin=open("27_B_17834.txt")
cl_a = []
cl_b = []
cl_c = []

for _ in range(9900):
    x,y = map(float,input().split())
    if x < 4 and y > 2:
        cl_a.append([x,y])
    elif x < 8 and y < 2:
        cl_b.append([x,y])
    else:
        cl_c.append([x,y])

xa,ya = func.func(cl_a)
xb,yb = func.func(cl_b)
xc,yc = func.func(cl_c)
print((xa+xb+xc)/3*100,(ya + yb+yc)/3*100)
#597 432
#408 352