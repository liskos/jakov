def f(s):
    while "333" in s:
        s = s.replace("333","4",1)
        s = s.replace("4444","3",1)
    return s

for n in range(1,101):
    s = "3" * n
    if f(s) == "43":
        print(n)

