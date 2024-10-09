import func27,sys
sys.stdin = open("27B_18031.txt")
cl_a = []
cl_b = []
cl_c = []
cl_d = []
cl_e = []
for _ in range(10000):
    x,y = map(float,input().split())
    if x > 12:
        cl_a.append([x,y])
    elif y < 4:
        cl_b.append([x,y])
    elif y < 10:
        cl_c.append([x,y])
    elif y < 14:
        cl_d.append([x,y])
    else:
        cl_e.append([x,y])
print(func27.f(cl_b,cl_c))
print(func27.f(cl_d,cl_e))
print(func27.f(cl_d,cl_c))

    #18166 26588