import itertools
b = set()
for a in (itertools.product("САМОКТ",repeat=7)):
    ss = "".join(a).replace("САМ","*")
    if ss.count("*") == 1 and "*" in ss[1:-1] and (ss[ss.find("*")-1] == ss[ss.find("*") + 1]) and ss[ss.find("*") - 1] in "АО":
        b.add(a)
print(len(b),b)
