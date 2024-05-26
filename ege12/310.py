def f(s):
    while ("111" in s) or ("222" in s):
        if "111" in s:
            s = s.replace("111", "22", 1)
        else:
            s = s.replace("222", "11", 1)
    return s

print(len(f("1" * 203 + "2")),f("2" + "1" * 203 ))