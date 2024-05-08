def f(s):
    while "333" in s:
        s = s.replace("333","4",1)
        s = s.replace("4444","3",1)
    return s

r = "43"
m = r.count("3") + r.count("4")
ma = m * 3

for i in range(m,ma + 1):
    s = "3" * i
    if f(s) == r:
        print(f"{i}")
