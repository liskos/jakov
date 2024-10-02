import itertools
b = set()
for a in (itertools.product("АНТИУОПЯ",repeat=16)):
    ss = "".join(a).replace("АНТИУТОПИЯ","1")
    if "1" in ss:
        b.add(a)
print(len(b))


#2 reshenie

import itertools,functools
b = set()
@functools.lru_cache(None)
def c(a):
    ss = "".join(a).replace("АНТИУТОПИЯ", "1")
    return "1" in ss


for a in (itertools.product("АНТИУОПЯ",repeat=16)):
    if c(a):
        b.add(a)
print(len(b))
