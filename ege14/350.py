
for x in "0123456789a":
    s1 = f"3364{x}"
    s2 = f"{x}7946"
    s = f"55{x}87"
    if int(s1,11) + int(s2,12) == int(s,14):
        print(int(s,14))