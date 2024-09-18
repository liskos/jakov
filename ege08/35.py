import itertools

s = set()
for i,a in enumerate(itertools.product("ДКМО",repeat=5),1):
    if "".join(a) == "ДОМОК" or "".join(a) == "КОМОД":
        print(i,a)

print(493-238)