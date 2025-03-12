def f(filename):
    file = open(filename)
    n = int(file.readline())
    a = [list(map(int,file.readline().split())) for _ in range(n)]
    v_magazine = [[0,0]]
    a = sorted(a,key=lambda x:(x[0],x[1]))
    m = 0
    k = 0
    was_peak = False
    for i in range(len(a)):
        v_magazine.append(a[i])
        min_exit = min(v_magazine, key=lambda x: x[1])[1]
        v_magazine = [x for x in v_magazine if x[1] > min_exit]
        m = max(m,len(v_magazine))
    v_magazine = [[0,0]]
    for i in range(len(a)):
        v_magazine.append(a[i])
        min_exit = min(v_magazine, key=lambda x: x[1])[1]
        v_magazine = [x for x in v_magazine if x[1] > min_exit]
        if len(v_magazine) == m:
            k += 1
    print(a)
    print(v_magazine)

    return k,m


print(f("130test.txt"))
print(f("26data/26-130.txt"))