def f(s):
    while ("=3" in s) or ("=4" in s) or ("=5" in s):
        if "=3" in s:
            s = s.replace("=3","55=")
        if "=4" in s:
            s = s.replace("=4","4=")
        if "=5" in s:
            s = s.replace("=5","3=")
    return s
a = []
for i in range(1,3000):
    s = "=" + "3" * 51 + "4" * i + "5" * 53
    b = f(s)
    b = b.replace("=","")
    if len(str(sum(map(int,b)))) == 4:
        a.append(i)

print(max(a))