a = [int(x) for x in open("17data/17-4.txt")]
r = []

average = sum(a) / len(a)

def f(x):
    return str(x).count("4") == 0
def d(x):
    return x < average
for i in range(len(a) - 1):
    if (d(a[i]) or d(a[i+1])) and (not(f(a[i])) and not(f(a[i+1]))):
        r.append(a[i] + a[i+1])

print(len(r), min(r))