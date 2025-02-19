import itertools

for i,a in enumerate(itertools.product("ГЕИНРСЯ",repeat=6),1):
    if "ГИРЯ" in "".join(a):
        print(i,a)