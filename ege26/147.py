def f(filename):
    file = open(filename)
    n = int(file.readline())
    a = [list(map(int,file.readline().split())) for _ in range(n)]
    a = sorted(a,key=lambda x:(x[0],x[1]))
    print(len(a), len(set([x[0] for x in a])))
    b = [[0] for _ in range(1000)]
    for t_pr, t_dos in a:
        t_okon = t_pr + t_dos
        vozmojnie = [i for i in range(len(b)) if b[i][-1] <= t_pr]
        perv = vozmojnie[0]
        b[perv].append(t_okon)
    ans1 = sum([1 for i in b if len(i) > 1])
    ans2 = len(b[0]) - 1
    return ans1, ans2


print(f("147test.txt"))
print(f("26data/26-147.txt"))