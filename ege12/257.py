def f(s):
    while ("xxx" in s) or ("zyx" in s) or ("zxx" in s):
        s = s.replace("xxx","zz",1)
        s = s.replace("zyx","x",1)
        s = s.replace("zxx","y")
    return s

s = "x" * 107

print(f(s))