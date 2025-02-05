def f(s):
    while ("1" in s):
        if "18" in s:
            s = s.replace("18","88881")
        else:
            s = s.replace("1","8888")
    return s


s = "1" + "8" * 70
d = f(s)
print(d.count("8"))