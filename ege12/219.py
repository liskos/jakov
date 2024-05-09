def f(s):
    while "111" in s:
        s = s.replace("11","2",1)
        s = s.replace("2222","111",1)
    return s

for n in range(82,1000):
    s = "1" * n
    if f(s) == "2221":
        print(n)
        break