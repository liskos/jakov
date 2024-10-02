import itertools
b = set()
for i,a in enumerate(itertools.permutations("ДЕЙНПТЬЯ",r=4),1):
    ss = "".join(a).replace("Е","Я")
    if ss.count("Я") == 0 and a.count("Ь") < 2 and a.count("Д") < 2 and a.count("Н") < 2 and a.count("Й") < 2 and a.count("П") == 1 and a.count("Т") == 1:
        print(a,i)