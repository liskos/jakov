def f(filename):
    file = open(filename)
    n = int(file.readline())
    a = [list(map(int,file.readline().split())) for _ in range(n)]
    dorogie = [x[1] for x in a]
    dorogie = sum(dorogie) / len(dorogie)
    lider = sorted([[x[0],x[1]] for x in a if x[2] == 0 and x[1] > dorogie],key=lambda x:x[0])

    print(lider)
    k = 0
    b = []
    for i in range(len(lider)-1):
        if lider[i][0] == lider[i+1][0]:
            k += 1
        else:
            b.append([lider[i][0],k,lider[i][1]])
            k = 0
            k += 1
    b.append([lider[i+1][0],k,lider[i+1][1]])
    b = sorted(b,key=lambda x:(-x[1],-x[2],-sum([1 for x in a if x[0] == b[0][0] and x[2] == 1])))
    print(b)
    print(a)
    otv1 = [x[1] for x in a if x[0] == b[0][0] and x[2] == 1]
    return sum(otv1),b[0][0]

# print(f("152test.txt"))
print(f("152test.txt"))
print(f("26data/26-153.txt"))