import itertools
b = set()
for i,a in enumerate(itertools.product("МАНОК",repeat=5),1):
    if "".join(a).count("М")==1 and "".join(a).count("А")==1 and "".join(a).count("Н")==1 and "".join(a).count("О")==1 and "".join(a).count("К")==1 and a[0] != "О" and "АО" not in "".join(a):
        b.add("".join(a))
print(len(b))

