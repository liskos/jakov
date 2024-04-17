for x in "0123456789abc":
    s1 = f"8{x}121"
    s2 = f"7{x}575"
    s = int(s1, 13) - int(s2, 13)
    if s  % 19 == 0:
        print(x, s // 19)
