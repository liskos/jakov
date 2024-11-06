a = [int(x) for x in open("17data/17-365.txt")]
r = []
b = []

def f(x):
    return x % 10 == 1

for i in range(len(r)-1):
    if f(a[i]) != f(a[i+1]) and max(a[i],a[i+1]) < max