import itertools

for i,a in enumerate(itertools.product("БИКНОПР",repeat = 6),1):
    if a.count("О") == 3 and a.count("Р") < 2 and a.count("Б") < 2 and a.count("П") < 2:
        print(i,a)