import itertools
b = set()
d = 26655
for i,a in enumerate(itertools.product("АИКЛМЬ",repeat=6),1):
    if a[0] == "К" and a[-1] == "Ь" and a.count("А") == 1 and a.count("И") == 1 and a.count("К") == 1 and a.count("Л") == 1 and a.count("М") == 1 and a.count("Ь") == 1:
        b.add(a)
        print(i)
print(len(b),b)