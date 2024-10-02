import itertools
b = set()
for a in (itertools.product("ВИДЕО",repeat=6)):
    ss = "".join(a)
    if a.count("И") > 0 and a.count("Е") > 0 and (ss.find("Е") < ss.find("И") < ss.find("О")) and (ss.rfind("Е") > ss.rfind("И") > ss.rfind("О")):
        b.add(a)

print(len(b),b)
