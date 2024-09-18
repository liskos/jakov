import itertools
b = set()
for i,a in enumerate(itertools.product("ЕЛНОСЦ",repeat=6),1):
    if i % 2 == 0 and a[0] != "Е" and a[0] != "О" and "".join(a).count("Ц") == 2:
        b.add(a)
print(len(b))

