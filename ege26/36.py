def f(filename):
    file = open(filename)
    n = int(file.readline())
    a = list(map(int,file.readline().split()))
    print(a)
    a = sorted(a)
    #
print(f("36test.txt"))







# desh = (a[:int(len(a)*0.7)])
    # skid1 = (a[int(len(a)*0.7):])
    # desh2 = (a[:int(len(a)*0.5)])
    # skid2 = (a[int(len(a)*0.5):])
    # if (sum(desh)*0.3)+(sum(skid1))*0.4 > (sum(desh2))*0.4+(sum(skid2))*0.35:
    #     n = max(skid1)*0.4
    # else:
    #     n = max(skid2)*0.35
    # return abs((sum(desh)*0.3)+(sum(skid1))*0.4 - (sum(desh2))*0.4+(sum(skid2))*0.35),n