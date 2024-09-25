import itertools
b = set()
for a in (itertools.permutations("АЙСБЕРГ",r=7)):
    ss = "".join(a).replace("А","Е")
    if a[0] != "Й" and ("ЙЕ" not in ss):
        b.add("".join(a))
print(len(b),b)

