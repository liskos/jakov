import operator
a = [int(x) for x in open("17data/17-295.txt")]
r = []
sr = sum(a) / len(a)

def f(c, b):
    result = 1
    s = map(int, str(c + b))
    for digit in s:
        result *= digit
    if result == 0:
        result = 1
    return (c + b) % result == 0 and (c + b) < max(a)

for i in range(len(a) - 1):
    if f(a[i], a[i + 1]):
        r.append(a[i]+a[i+1])

print(len(r),max(r))