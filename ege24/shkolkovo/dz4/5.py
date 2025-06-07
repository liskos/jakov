s = open("files/24_3__6ao05.txt").read()

for ch in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
    s = s.replace(ch,"1")
s = s.split("1")
print(s)


def prost(n):
    a = [True] * 50000
    a[0] = False
    a[1] = False
    for i in range(2, 50000):
        if a[i]:
            for g in range(i ** 2, 50000, i):
                a[g] = False

    r = [i for i in range(50000) if a[i]]
    return r


pr = prost(1)
k = 0
for i in range(len(s)):
    if s[i].isdigit() and int(s[i]) in pr:
        k += 1

print(k)





