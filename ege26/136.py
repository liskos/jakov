def f(filename):
    file = open(filename)
    n,m = map(int,file.readline().split())
    slovar = dict()
    for _ in range(n):
        stoim, prod = map(int,file.readline().split())
        slovar[stoim] = slovar.get(stoim, [0,0])   # 1:2  1 - продан   2 - непродано
        if prod == 0:
            slovar[stoim] = [slovar[stoim][0], slovar[stoim][1] + 1]
        else:
            slovar[stoim] = [slovar[stoim][0] + 1, slovar[stoim][1]]
    print(slovar)
    dorogie = []
    deshevo = []
    for i in slovar:
        if i > m:
            dorogie.append([i,slovar[i][0],slovar[i][1]])
        else:
            deshevo.append([i,slovar[i][0],slovar[i][1]])
    print(dorogie)
    print(deshevo)
    pop_dorogie = max(dorogie,key=lambda x:x[1])
    pop_deshevo = max(deshevo,key=lambda x:x[1])
    print(pop_deshevo,pop_dorogie)
    ans1 = pop_deshevo[0] * pop_deshevo[1] + pop_dorogie[0] * pop_dorogie[1]
    ans2 = pop_deshevo[2] + pop_dorogie[2]
    return ans1,ans2
print(f("136test.txt"))
print(f("26data/26-136.txt"))