import itertools
for i,a in enumerate(itertools.product("АВНРЬЯ",repeat=5),1):
    if a[0] != "Я" and a.count("Ь")==1 and "".join(a).count("ЯЯ") == 0:
        print(a,i)