a = [int(x) for x in open("17data/17-243.txt")]
r = []
b = [x for x in a if x % 173 == 0]
def f(x):
    return x > max(b)
def d(x):
    t = "012"
    s = ""
    while x > 0:
        s = t[x%3] + s
        x //= 3
    return s.count("22") > 0


for i in range(len(a) - 1):
    if (f(a[i]) or f(a[i+1])) and (d(a[i]) or d(a[i+1])) :
        r.append(a[i] + a[i+1])

print(len(r), min(r))