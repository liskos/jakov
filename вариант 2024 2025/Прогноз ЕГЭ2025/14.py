import string
for x in "0123456789abcdefghijk":
    s1 = int(f"{x}5B{x}8",21)
    s2 = int(f"H053{x}7",21)
    s = s1 + s2
    if s % 12 == 0:
        print(x,s//12)
