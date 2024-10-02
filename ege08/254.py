import itertools
b = set()
for i,a in enumerate(itertools.product("0123456789abcdef",repeat=5),1):
    ss = "".join(a).replace("3b","l")
    if a[0] == "f" and a[-1] == "a" and ss.count("l") == 1:
        b.add(a)
print(len(b),b)