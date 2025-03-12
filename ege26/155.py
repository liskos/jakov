def f(filename):
    file = open(filename)
    n = int(file.readline())
    a = [list(map(int,file.readline().split())) for _ in range(n)]
    a = sorted(a,key=lambda x: (x[0],x[2]))
    print(a[:30])
    shtrafi = [[a[x][0],a[x][1]+a[x+1][1],a[x][2]] for x in range(len(a)-1) if a[x][0] == a[x+1][0] and a[x][2] == a[x+1][2]]
    shtrafi2 = [x for x in a if shtrafi.count(x) == 0]
    shtrafi += shtrafi2
    ans = max(shtrafi, key=lambda x:(x[1],-x[0],-x[2]))

    return ans



print(f("155test.txt"))
print(f("26data/26-155.txt"))