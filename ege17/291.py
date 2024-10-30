a = [int(x) for x in open("17data/17-290.txt")]
r = []


def d(v,b,c):
    return v % 5 == 4 or b % 5 == 4 or c % 5 == 4
def f(v,b,c):
    return hex(v)[2:].count("0") == 0 and hex(b)[2:].count("0") == 0 and hex(c)[2:].count("0") == 0

for i in range(len(a)-2):
    if f(a[i],a[i+1],a[i+2]) and d(a[i],a[i+1],a[i+2]):
        r.append(max(a[i],a[i+1],a[i+2]) - min(a[i],a[i+1],a[i+2]))

print(len(r),max(r))