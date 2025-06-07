a = [int(x) for x in open("17_20963.txt")]
r = []
b = min([x for x in a if len(str((abs(x)))) == 4 and abs(x) % 17 == 0])

def f(x):
    return len(str(abs(x))) == 4 and abs(x) % 100 == 27
for i in range(len(a)-2):
    if (f(a[i]) or f(a[i+1]) or f(a[i+2])) and ((a[i] ** 2) + (a[i+1] ** 2) + (a[i+2] ** 2)) <= b ** 2:
        r.append(abs(a[i])+abs(a[i+1])+abs(a[i+2]))

print(len(r),min(r))



print(int((21) // 1.5))