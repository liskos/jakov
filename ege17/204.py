a = [int(x) for x in open("17data/17-204.txt")]
r = []

def f(x):
    return 0 < x and x % 10 == 9


for i in range(len(a)-2):
    if not(f(a[i])) and f(a[i+1]) and not(f(a[i+2])):
        r.append(a[i]+a[i+1]+a[i+2])

print(len(r),max(r))