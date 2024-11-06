a = [int(x) for x in open("17data/17-390.txt")]
b = max([x for x in a if abs(x) % 100 == 73])
r = []

def f(x):
    return len(str(abs(x))) == 3

def d(x,y,z):
    return x % 11 == 0 or y % 11 == 0 or z % 11 == 0



for i in range(len(a)-2):
    if (int(f(a[i])) + int(f(a[i+1])) + int(f(a[i+2]))) == 2 and d(a[i],a[i+1],a[i+2]) and (a[i]+a[i+1]+a[i+2]) > b:
        r.append(a[i]+a[i+1]+a[i+2])


print(len(r),max(r))