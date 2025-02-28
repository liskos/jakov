def f(filename):
    file = open(filename)
    n,t = map(int,file.readline().split())
    v = [list(map(int,file.readline().split())) for _ in range(n)]
    sr = sum(v[x][0] for x in range(len(v)))/len(v)
    sr = (int(sr+0.9999))
    sv = [v[x][1] for x in range(len(v)) if v[x][0] >= sr]
    sv = sorted(sv)
    print(sv)
    v = [v[x][0] for x in range(len(v)) if v[x][0] < sr]
    s = sum(sv[:len(v)])



    return len(v)*2,s
print(f("68test.txt"))
print(f("26data/26-68.txt"))