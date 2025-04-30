def f(s):
    while (">3" in s) or (">5" in s) or (">7" in s):
        if ">3" in s:
            s = s.replace(">3","55>")
        if ">5" in s:
            s = s.replace(">5","5>3")
        if ">7" in s:
            s = s.replace(">7","3>5")

    return s


s = ">" + "3" * 10 + "5" * 10 + "7" * 10
s = f(s)
s = s.replace(">","")
print( sum(map(int,s)))


