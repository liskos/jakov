def f(s):
    while "32" in s:
        s = s.replace("32","6",1)
    return s

for i in range(1, 30):
    s = "32" * 8 + "3" * (i-8)
    print(i, sum(map(int,f(s))), f(s))