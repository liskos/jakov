def f(s):
    while "411" in s or "1111" in s:
        if "411" in s:
            s = s.replace("411","14",1)
        if "1111" in s:
            s = s.replace("1111","1",1)
    return s

b = set()
for i in range(4,10000):
    s = "4" + "1" * i
    b.add(sum(map(int,f(s))))
print(max(b))