def f(s):
    while ("-=" in s) or ("2++" in s) or ("++++" in s):
        if "-+" in s:
            s = s.replace("-+","2+",1)
        if "2++" in s:
            s = s.replace("2++","--",1)
        if "++++" in s:
            s = s.replace("++++","22",1)
    return s.count("+") + s.count("-")

for i in range(1,1000):
    s = "-" + "+" * i
    if f(s) == 251:
        print(i)