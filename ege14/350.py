
for x in "0123456789abcdefgh":
    s1 = f"9009{x}"
    s2 = f"2257{x}"
    s = int(s1, 18) + int(s2, 18)
    if s  % 15 == 0:
        print(x, s // 15)

