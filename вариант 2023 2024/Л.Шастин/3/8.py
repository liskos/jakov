import itertools
z = []
for i in itertools.product("01234567", repeat=7):
    s = "".join(i).replace("2", "0").replace("4", "0").replace("6", "0")
    if i[0] != "0" and s.count("0") == 2 and all(((x+"7" not in s) and ("7"+x not in s)) for x in "1357"):
        z.append(i)
print(len(z))
