def f(s):
    while "25" in s:
        s = s.replace("25","9",1)
    return s

for i in range(1, 13):
    s = "25" * i + "5" * (12-i)
    print(i, sum(map(int,f(s))), f(s))

for i in range(13, 30):
    s = "25" * 12 + "2" * (i-12)
    print(i, sum(map(int,f(s))), f(s))