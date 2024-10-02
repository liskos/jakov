import itertools
b = set()
for a in itertools.permutations("ЛОГАРИФМ",r=5):
    ss = "".join(a).replace("Л","М").replace("Г","М").replace("Р","М").replace("Ф","М")
    ss = ss.replace("О","И").replace("А","И")
    if "ММ" not in ss and "ИИ" not in ss:
        b.add(a)
print(len(b),b)


