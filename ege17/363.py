a = [int(x) for x in open("17data/17-363.txt")]
r = []
b = min(x for x in a if abs(x) % 100 == 40)



def f(x):




for i in range(len(a)-2):
    if f(a[i],a[i+1],a[i+2]):
        r.append([a[i],a[i+1],a[i+2]])

print(len(r),len(r)*3)