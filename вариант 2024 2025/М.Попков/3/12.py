def f(s):
    while ("444" in s) or ("777" in s):
        if "777" in s:
            s = s.replace("777","4",1)
        else:
            s = s.replace("444","7",1)
    return s

b = []
for i in range(4,10000):
    s = "4" + "7" * i
    v = sum(map(int,f(s)))
    b.append(v)

print(max(b))