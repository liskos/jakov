def f(filename):
    file = open(filename)
    n = int(file.readline())
    a = [int(file.readline()) for _ in range(n)]
    ydovl = sorted([x for x in a if x > 401])
    k = int(len(ydovl) / 3)
    skid  = ydovl[:k]
    a = [x for x in a if skid.count(x) == 0]
    skid1 = sum(skid)*0.75


    return int((sum(a)+skid1)+0.9999),max(skid)









print(f("26data/26_3__40zyf.txt"))