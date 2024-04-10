
for x in "0123456789abcde":
    s1 = f"123{x}5"
    s2 = f"1{x}233"
    s = int(s1, 15) + int(s2, 15)
    if s  % 14 == 0:
        print(x, s // 14)