a = [int(x) for x in open("17_17939.txt")]
r = []
d = 0
b = ([d+1 for x in a if x < 0 and x % 5 == 0])
print(b)
def f(x):
    return len(str(abs(x))) == 4

for i in range(len(a)-2):
    if (int(a[i]) + int(a[i+1]) + int(a[i+2])) > 1 and (a[0] + a[1] + a[2]) >= sum(b):
        r.append(a[i] + a[i+1] + a[i+2])

print(len(r),min(r))