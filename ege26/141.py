def f(filename):
    file = open(filename)
    n = int(file.readline())
    a = [list(map(int,file.readline().split())) for _ in range(n)]
    ans2 = min(a,key=lambda x:x[1])
    b = [ans2]
    while True:
        vozmojne = [[a1,a2] for a1,a2 in a if b[-1][1] <= a1 ]
        if not vozmojne:
            break
        ranni_yrok = min(vozmojne,key=lambda x:x[1])
        b.append(ranni_yrok)
    return len(b), ans2[1]




print(f("141test.txt"))
print(f("26data/26-141.txt"))