import itertools
b = set()
for a in (itertools.permutations("ЧИУАУА",r=6)):
        b.add("".join(a))
print(len(b),b)

