def f(filename):
    file = open(filename)
    n,k = map(int,file.readline().split())
    a = [list(map(int,file.readline().split())) for _ in range(n)]
    b = [[1,1]]
    while True:
        vozmosjnie = [[a1,a2] for a1,a2 in a if a1 <= b[-1][1] <= a2  ]
        if not vozmosjnie or b[-1][1] >= k:
            break
        right_f = max(vozmosjnie,key=lambda x:x[1])
        b.append(right_f)
    ans2 = 0
    for a1,a2 in a:
        if a1<=k<=a2:
            ans2 += 1
    print(b)
    return len(a) - (len(b) - 1),ans2




print(f("139test.txt"))
print(f("26data/26-139.txt"))