for x in "0123456789abcde":
    s1 = f"82{x}19"
    s2 = f"6{x}073"
    s = int(s1, 15) - int(s2, 15)
    if s  % 11 == 0:
        print(x, s // 11)
