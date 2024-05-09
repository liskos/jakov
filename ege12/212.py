def f(s):
    while "111" in s:
            s = s.replace('111',"2",1)
            s = s.replace('222','1',1)
    return s

for n in range(61,1000):
    s = n * "1"
    if f(s) == "221":
        print(n)
        break
