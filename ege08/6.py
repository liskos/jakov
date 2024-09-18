import itertools
for i,a in enumerate(itertools.product("АКРУ",repeat=5),1):
    if i == 250:
        print("".join(a),i)
