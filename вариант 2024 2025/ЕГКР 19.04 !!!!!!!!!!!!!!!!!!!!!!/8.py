import itertools

for i,a in enumerate(itertools.product("АБДЕОП",repeat=6),1):
    if a[0] == "О" and len("".join(a)) == len(set("".join(a))):
        print(a,i)