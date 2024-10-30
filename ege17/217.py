a = [int(x) for x in open("17data/17-1.txt")]
r = []

average = sum(a) / len(a)

def f(x):
    return x < average

for i in range(len(a) - 1):
    if ((abs(a[i]) % 100 == 13) or (abs(a[i+1]) % 100 == 13)) and (f(a[i]) or f(a[i+1])):
        r.append(a[i] + a[i+1])

print(len(r), max(r))