def f(s):
    while (">1" in s) or (">2" in s) or (">3" in s):
        if ">1" in s:
            s = s.replace(">1","22>3",1)
        if ">2" in s:
            s = s.replace(">2","2>",1)
        if ">3" in s: s = s.replace(">3","11>2",1)
    return s


s = ">" + "1" * 14 + "2" * 20 + "3" * 25
b = ">" + "4" * 50
s = f(s)
s = s.replace(">","")
b = f(b)
b = b.replace(">","")
print(sum(map(int,s)))
print(sum(map(int,b)))