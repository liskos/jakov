def f(filename):
    file = open(filename)
    k,n = map(int,file.readline().split())
    mest = [[int(file.readline()),_+1] for _ in range(k)]
    st = [list(map(int, file.readline().split())) for _ in range(n)]
    st = sorted(st,key=lambda x:-x[0])
    print(st[:30])
    for x in range(len(st)):
        if mest.count(st[x][1]):



print(f("26data/26-61.txt"))