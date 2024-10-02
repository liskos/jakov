import itertools
b = set()
for a in itertools.product("СОЛНЦЕ",repeat=6):
    if a.count("О") < 3 and a.count("Ц") == 1:
        b.add(a)

print(len(b),b)