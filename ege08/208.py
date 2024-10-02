import itertools
b = set()
for a in itertools.permutations("ДЕЙКСТРА",r=6):
    ss = "".join(a).replace("Е","А")
    if a.count("Й") == 1 and "ЙА" not in ss:
        b.add(a)


print(len(b),b)