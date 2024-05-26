def f(s):
    while ("3333"  in s) or ("222"  in s):
        if "3333" in s:
          s = s.replace("3333","2",1)
        else:
          s = s.replace("222","3",1)
    return s

for i in range(1,100):
    s = "3" * i
    if f(s) == "22":
        print(i)

