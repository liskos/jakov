import func27,sys
sys.stdin = open("27.txt")
cl_a = []
cl_b = []
for _ in range(96):
    x,y = map(float,input().split())
    if x < 1:
        cl_a.append([x,y])
    else:
        cl_b.append([x,y])

print(func27.f(cl_a, cl_b))
#1731 6256