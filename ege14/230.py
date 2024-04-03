 for x in "0123456789abcdefghi":
    s1 = f"55{x}36"
    s2 = f"{x}2724"
    s = int(s1, 19) + int(s2, 19)
    if s  % 11 == 0:
        print(x, s // 11)

 for x in '01234567':
    s = (88 + 2 * 8 ** )