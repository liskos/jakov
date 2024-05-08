def f(s):
    while "111" in s:
        s = s.replace("11","2",1)
        s = s.replace("2222","111",1)
    return s

r = "2221"
m = r.count("1") + r.count("2")
max = m * 3

for i in range(m,max + 1):
    s = "1" * i
    if f(s) == r:
        print(f"{i}")
        break