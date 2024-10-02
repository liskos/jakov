import itertools
b = set()
for a in itertools.permutations("АПЕЛЬСИН",r=7):
    ss = "".join(a).replace("П","Н").replace("Л","Н").replace("С","Н")
    if "НЬН" in ss or a.count("Ь")==1:
        b.add(a)


print(len(b))