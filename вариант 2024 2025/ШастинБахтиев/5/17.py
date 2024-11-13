a = [int(x) for x in open("17 (2).txt")]

r = []
b = min([x for x in a if abs(x) % 10 == 7])

def f(n):
    return len(str(abs(n))) == 5
for i in range(len(a)-2):
    if (f(a[i]) or f(a[i+1]) or f(a[i+2])) and (a[i]*a[i+1]*a[i+2]) % b == 0:
        r.append(a[i]*a[i+1]*a[i+2])

print(len(r),max(r))