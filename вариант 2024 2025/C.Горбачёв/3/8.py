import itertools,string
s = set()
for a in itertools.product("0123456789abcdef",repeat=5):
    if a[0] != "0":
        if (a[0] not in "13579bdf") and (a[-1] not in "02468ace") and len(set("".join(a))) == 5:
            s.add(a)


print(s)
print(len(s))
