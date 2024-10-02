import itertools

def d(n):
    s = ""
    t = "0123456789ab"
    while n > 0:
        s = t[n%12] + s
        n //= 12
    return s

b = set()
for a in (itertools.permutations("СПОРТЛОТО",r=9)):
    if "ОО" in "".join(a):
        b.add(a)
print(len(b),b)
