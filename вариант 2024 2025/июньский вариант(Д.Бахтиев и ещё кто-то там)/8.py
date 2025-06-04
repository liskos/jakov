import itertools
b = set()
for i,a in enumerate(itertools.product("АБЕИЛРТФЦ",repeat=5),1):
    if (i % 2 != 0) and (a[0] not in "АЕИ") and (a.count("Ц") == a.count("Ф")):
        b.add(a)

print(len(b),b)