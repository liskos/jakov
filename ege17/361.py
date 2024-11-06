a = [int(x) for x in open("17data/17-361.txt")]
r = []
b = min(x for x in a if abs(x) % 100 == 40)



def f(x,y,z):
    return ((x == y and z != y) or (x == z and y != z) or (y == z and x!= y)) and min(x,y,z) > b




for i in range(len(a)-2):
    if f(a[i],a[i+1],a[i+2]):
        r.append([a[i],a[i+1],a[i+2]])

print(len(r),len(r)*3)