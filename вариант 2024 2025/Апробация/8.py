import itertools

for i,a in enumerate(itertools.product("КОСУФ",repeat=5),1):
    if a.count("Ф") == 0 and a.count("У") == 2:
        print(a,i)