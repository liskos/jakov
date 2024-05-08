def f(s):
    while "66" in s:
        s = s.replace("66","1",1)
        s = s.replace("11","2",1)
        s = s.replace("22","6",1)
    return s

r = "21"
m = r.count("1") + r.count("2") + r.count("6")
ma = m * 3

for i in range(m,ma + 1):
    s = "6" * i
    if f(s) == r:
        print(f"{i}")
