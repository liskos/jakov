def min_t(mass):
    mass.sort()
    m = 10 ** 10
    for i in range(len(mass)-1):
        m = min(mass[i+1]-mass[i], m)
    return m


def f(filename):
    file = open(filename)
    n = int(file.readline())
    b = []
    for _ in range(n):
        x, y, t = map(int,file.readline().split())
        for i in range(len(b)):
            if b[i][0] == x and b[i][1] == y:
                b[i][2].append(t)
                break
        else:
            b.append([x, y, [t]])
    print(b)
    best_x = 0
    best_y = 0
    best_t = 10**10
    for x, y, t in b:
        if min_t(t) <= best_t and len(t) >= 2:
            best_t = min_t(t)
            best_x = x
            best_y = y
    print(best_x, best_y, best_t)



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
