def f(filename):
    file = open(filename)
    n,k = map(int,file.readline().split())
    a = [list(map(int,file.readline().split())) for _ in range(n)]
    print(a)
    print(k)
    # for i in range(len(a)-1):


print(f("67test.txt"))
print(f("26data/26-66.txt"))