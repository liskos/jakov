import itertools
b = set()
for a in itertools.product("СИРОП",repeat=5):
    if a.count("О") == 1 and "ИО" not in "".join(a) and a[0] != "О" :
        b.add(a)
print(len(b),b)


