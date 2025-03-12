def f(filename):
    file = open(filename)
    n = int(file.readline())
    a = [list(map(int,file.readline().split())) for _ in range(n)]
    a = sorted(a,key=lambda x:(x[0],x[1]))
    print(a)
    b = []
    k = 0
    ans1 = 0
    ans2 = []
    for i in range(len(a)):
        b.append(a[i][1]-a[i][0])
        if i != 0 and a[i][0] <= a[i-1][1]:
            b.append(abs(max[i][1]-a[i-1][1]))
    for i in range(len(a)-1):
        if a[i][1] == a[i+1][0]:
            k += 1
            ans2.append(a[i+1][1]-a[i][0])
        else:
            k *= 50
    print(ans2)
    return sum(b),




print(f("140test.txt"))