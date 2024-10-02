import itertools
b = set()
for a in itertools.product("АБВГД",repeat=3):
    s = "".join(a).replace("А","1").replace("Б","2").replace("В","3").replace("Г","4").replace("Д","5")
    if s[0] < s[1] and s[1] < s[2]:
        b.add(a)
print(len(b),b)