
for x in "0123456789abcdefg":
    s1 = f"9759{x}"
    s2 = f"3{x}108"
    s = int(s1, 17) + int(s2, 17)
    if s  % 11 == 0:
        print(x, s // 11)

