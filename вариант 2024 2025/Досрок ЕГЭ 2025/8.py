import itertools
b = set()
for a in itertools.product("ДГИАШЭ",repeat=5):
    if a[0] not in "ИАЭ" and a[-1] not in "ДГШ":
        b.add(a)


print(len(b),b)