def sol(s):
    import sys
    sys.stdin = open(s)
    n = int(input())
    stud = dict()
    for i in range(n):
        id,number = map(int,input().split())
        stud[id] = stud.get(id,[]) + [number]
    for m in stud:
        stud[m] = sorted(set(stud[m]))
    max_len = dict()
    for id in stud:
        t = stud[id]
        k = 1
        m = 1
        for i in range(1,len(t)):
            if t[i] == t[i-1]+1:
                k += 1
                m = max(m, k)
            else:
                k = 1
        max_len[id] = m
    m = max(max_len.values())
    a = [id for id in max_len if max_len[id]== m]
    # print(m)
    # print(max_len)
    # print(stud)
    #print(a)
    return min(a),m


if __name__ == "__main__":
    print(*sol("26_19256.txt"))