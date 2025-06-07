def f(filename):
    file = open(filename)
    n,km = map(int,file.readline().split())
    a = [list(map(int,file.readline().split())) for _ in range(n)]
    print(a)
    # m = [[]] * km
    m = [[] for _ in range(km)] # мастерские
    print(m)
    musor = [] #утилизация
    k = 0  #счёт работ за день
    a = sorted(a,key=lambda x:(x[0]))
    for i in a:
        minim_len_materskya = m.index((min(m,key=len)))   # индекс той,где меньше единиц техники
        if i[2] == 0:
            m[minim_len_materskya] = [b for b in m[minim_len_materskya] if i[0] < b]
            if len(m[minim_len_materskya]) == 5:
                musor.append(1)
            else:
                m[minim_len_materskya].append(i[1])
                k += 1
        else:
            m[i[2]-1] = [b for b in m[i[2]-1] if i[0] < b]
            if len(m[i[2]-1]) == 5:
                    musor.append(1)
            else:
                m[i[2]-1].append(i[1])
                k += 1
    print(m)
    return k,sum(musor)



print(f("26test.txt"))
print(f("26_20970.txt"))