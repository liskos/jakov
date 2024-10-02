import itertools
b = set()
for a in itertools.permutations("ЗЕРКАЛОКККК",r=6):
    if a.count("К") < 5:
        b.add(a)

print(len(b))