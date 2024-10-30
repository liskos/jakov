a = [int(x) for x in open("17data/17-4.txt")]
r = []

average = sum(a) / len(a)

def f(x):
    return x % 7 == 0 and x % 3 != 0 and x % 11 != 0 and x % 13 != 0
def d(x):
    return x < average
for i in range(len(a) - 1):
    if (f(a[i]) or f(a[i+1])) and (d(a[i]) or d(a[i+1])):
        r.append(a[i] + a[i+1])

print(len(r), min(r))