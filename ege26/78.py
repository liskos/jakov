def f(filename):
    file = open(filename)
    n,start,end = map(int,file.readline().split())
    a = [list(map(int,file.readline().split())) for _ in range(n)]
    otv1 = a[0][1] - start + 1
    a = sorted(a,key=lambda x:x[1])
    print(a)
    k = 0
    for i in range(len(a)-1):
        if a[i][1] > a[i+1][0] and a[i][0] != a[i+1][0]:
            k += 1


    return otv1,k



print(f("78test.txt"))
print(f("26data/26-78.txt"))