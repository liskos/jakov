a = [int(x) for x in open("17data/17-370.txt")]
r = []
b = [x for x in a if str(abs(x)) == str(abs(x))[::-1] and len(str(abs(x))) == 3]

def f(x):
    return len(str(abs(x))) == 4


for i in range(len(a)-1):
    if f(a[i]) != f(a[i+1]) and (((a[i] ** 2) + (a[i + 1] ** 2))) % min(b) == 0:
        r.append((a[i] ** 2) + (a[i + 1] ** 2))

print(len(r),max(r))