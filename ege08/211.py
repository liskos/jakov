import itertools
b = set()
for a in itertools.permutations("ТИКТОК",r=6):
    if "КК" not in "".join(a) and "ТТ" not in "".join(a):
        b.add(a)

print(len(b),b)