import itertools
b = set()
for a in itertools.permutations("ЕСАУЛ",r=5):
    ss = "".join(a).replace("Е","У").replace("А","У")
    if "УУ" not in ss:
        b.add("".join(a))
print(len(b),b)