import itertools

s = set()
for a in itertools.product("МЕТРО",repeat=4):

    if a[0] in "МТР" and a[-1] in "ЕО":
        s.add(a)
print(len(s))