import itertools
b = []
for a in itertools.product("01",repeat=20):
    if len(str(int("".join(a),2))) == 6:
        b.append(a.count("0"))


print(max(b))