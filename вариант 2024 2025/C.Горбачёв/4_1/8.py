s = set()
import itertools
for a in itertools.product("0123456",repeat = 7):
    if a[0] not in "035":
        if a[-1] not in "0246" and a.count("0") < 2:
            s.add(a)

print(len(s))