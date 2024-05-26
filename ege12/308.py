def f(s):
    while ("22222" in s) or ("9999" in s):
        if "22222" in s:
            s = s.replace("22222", "99", 1)
        else:
            s = s.replace("9999", "2", 1)
    return s

print(f("9" * 96))