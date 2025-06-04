def f(filename):
    file = open(filename)
    n = int(file.readline())
    a = [list(map(int,file.readline().split())) for _ in range(n)]
    a = sorted(a,key=lambda x:(x[0],x[1],x[2]))
    b = []
    for i in range(len(a)-1):
        if a[i][0] == a[i+1][0] and a[i][1] == a[i+1][1]:
            b.append([a[i][0],a[i][1],a[i+1][2]-a[i][2]])
    print(b)
    b = [d for d in b if (d[0] - d[1]) != 0]
    b = sorted(b,key=lambda x:(x[0],x[1],x[2]))[0]
    return b[0] + b[1],b[2]



print(f("26test.txt"))
print(f("26_22605.txt"))


# def f(filename):
#     file = open(filename)
#     n = int(file.readline())
#     a = [list(map(int,file.readline().split())) for _ in range(n)]
#     a = sorted(a,key=lambda x:(x[0],x[1],x[2]))
#     b = []
#     for i in range(len(a)-1):
#         if a[i][0] == a[i+1][0] and a[i][1] == a[i+1][1]:
#             b.append(a[i])
#             b.append(a[i+1])
#     print(b)
#     b = [[b[d][0],b[d][1],b[d+1][2] - b[d][2]] for d in range(len(b)-1) if (b[d][0] - b[d][1]) != 0 and b[d][2] != b[d+1][2]]
#     print(b)
#     b = sorted(b,key=lambda x:(x[0],x[1],x[2]))[0]
#     return b[0] + b[1],b[2]
#
#
#
# print(f("26test.txt"))
# print(f("26_22605.txt"))
