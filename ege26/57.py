def f(filename):
    file = open(filename)
    n,m = map(int,file.readline().split())
    a = list(map(int,file.readline().split()))
    print(a)




print(f("57test.txt"))