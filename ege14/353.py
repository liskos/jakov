
for x in "0123456789abcdefg":
    s1 = f"66{x}63"
    s2 = f"5{x}810"
    s = int(s1, 17) - int(s2, 17)
    if s  % 11 == 0:
        print(x, s // 11)

