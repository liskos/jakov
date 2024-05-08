def f(s):
    while "111" in s:
        s = s.replace("111","2",1)
        s = s.replace("222","3",1)
        s = s.replace("333","1",1)
    return s

r = "321"
m = r.count("1") + r.count("2") + r.count("3")
ma = m * 3

res = set()
for i in range(1,101):
    s = "1" * i
    if f(s) == r:
        res.add(f(s).count('1'))
print(res)

