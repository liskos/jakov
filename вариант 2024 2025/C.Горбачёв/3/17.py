a = [int(x) for x in open("17.txt")]
r = []


def f(a1,b,c):
    return int(abs(a1)% 11 == 0 and abs(a1) % 10 == 3) + int(abs(b)% 11 == 0 and abs(b) % 10 == 3) + int(abs(c)% 11 == 0 and abs(c) % 10 == 3)

for i in range(len(a)-2):
    if f(a[i],a[i+1],a[i+2]) == 2:
        print(a[i],a[i+1],a[i+2])
        r.append(2*(a[i]+a[i+1]+a[i+2]))


print(len(r),min(r))