import itertools
b = set()
for a in itertools.permutations("ВОЛКОДАВ",r=8):
    ss = "".join(a).replace("Л","В").replace("К","В").replace("Д","В")
    ss = ss.replace("О","А")
    if ("АА" in ss) or ("ВВ" in ss):
        b.add(a)

print(len(b),b)