a = [int(x) for x in open("17data/17-243.txt")]
r = []
b = max([x for x in a if x % 127 == 0])



def f(x):
    return x > b
def d(x):
    return (oct(x)[2:]).count("31") > 0
for i in range(len(a) - 1):
    if (f(a[i]) or f(a[i+1])) and (d(a[i]) or d(a[i+1])) :
        r.append(a[i] + a[i+1])

print(len(r), min(r))