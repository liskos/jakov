import itertools
b = set()
for a in (itertools.permutations("НОБЕЛИЙ",r=7)):
    if (a[0] != "Й") and ("ИЙО" not in "".join(a)):
        b.add("".join(a))
print(len(b))

