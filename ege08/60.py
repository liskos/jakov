import itertools
b = set()
for a in itertools.product("АБВГЭЮЯ",repeat=5):
    if a[0] == "Э" or a[0] == "Ю" or a[0] == "Я" and a[-1] == "Э" or a[-1] == "Ю" or a[-1] == "Я" and(a[1] != "Э" and a[1] != "Я" and a[1] != "Ю" and a[2] != "Э" and a[2] != "Я" and a[2] != "Ю" and a[3] != "Э" and a[3] != "Я" and a[3] != "Ю"):
        b.add(a)
print(len(b),b)


print("".join(a)[1:-1])