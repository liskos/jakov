for x in "0123456789abcdefghijkl":
    s1 = f"98{x}79641"
    s2 = f"36{x}14"
    s3 = f"73{x}4"
    s = int(s1,22) + int(s2,22) + int(s3,22)
    if s % 21 == 0:
        print(x,s // 21)