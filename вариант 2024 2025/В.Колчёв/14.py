k = 0
for x in "123456789abcdefghijklmno":
    s1 = int(f"8af7{x}11",25)
    s2 = int(f"{x}DA87",25)
    s = s1 + s2
    if s % int(x,25) == 0:
        k += 1

print(k)