def f(filename):
    file = open(filename)
    n,km = map(int,file.readline().split())
    a = [list(map(int,file.readline().split())) for _ in range(n)]
    m = [[] for _ in range(km)] # мастерские
    musor = [] #утилизация
    a = sorted(a,key=lambda x:(x[0], x[0]+x[1]))
    for t_b, t_r, rem in a:
        if rem == 0:
            t = []
            for i in range(km):
                t.append(len([1 for x in m[i] if x > t_b]))
            t = t.index(min(t)) # номер мастерской с мин количеством устройств в ремонте
            if len([1 for x in m[t] if x > t_b]) >= 5:
                musor.append(1)
            else:
                m[t].append(max(m[t]+ [t_b])+t_r)
        else:
            if len([1 for x in m[rem-1] if x > t_b]) >= 5:
                musor.append(1)
            else:
                m[rem-1].append(max(m[rem-1]+[t_b])+t_r)
    k1 = max([len(x) for x in m])
    k2 = len(musor)
    return k1, k2





















  #       if rem == 0:
  #           ind = km
  #           for x in range(km):
  #               ind = min(ind, len([t for t in m[x] if t > t_b]))
  #           m_ind = 0
  #           for x in range(km):
  #               if len([t for t in m[x] if t > t_b]) == ind: m_ind = x
  # # индекс той,где min единиц техники
  #           if len([b for b in m[m_ind] if t_b < b]) == 5:
  #               musor.append(1)
  #           else:
  #               m[m_ind].append(t_b + t_r)
  #       else:
  #           if len([b for b in m[rem-1] if t_b < b]) == 5:
  #                   musor.append(1)
  #           else:
  #               m[rem-1].append(t_b + t_r)
  #   print(m)

    return len(max(m,key=len)),sum(musor)



print(f("26test.txt"))
print(f("26_20970.txt"))