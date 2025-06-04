k = set()
for x in "123456789abcdefghijklmno":
    s1 = int(f"8af7{x}11",25)
    s2 = int(f"{x}DA87",25)
    s = s1 + s2
    for y in range(1,101):
        if s % y == 0:
            k.add(y)

print(len(k))