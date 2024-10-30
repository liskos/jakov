a = [int(x) for x in open("17data/17-294.txt")]
r = []
sr = sum(a) / len(a)
def f(c, b):
    return (sum(map(int, str(c))) + sum(map(int, str(b)))) ** 0.5 == int((sum(map(int, str(c))) + sum(map(int, str(b)))) ** 0.5) and (c + b) > sr


for i in range(len(a) - 1):
    if f(a[i], a[i + 1]):
        r.append(a[i]+a[i+1])

print(len(r),max(r))