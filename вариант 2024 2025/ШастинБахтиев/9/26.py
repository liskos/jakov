
def f(filename):
    file = open(filename)
    n = int(file.readline())
    s = [list(map(int,file.readline().split())) for _ in range(n)]
    chet = [[s[x][0],s[x][1]] for x in range(len(s)) if s[x][1] % 2 == 0]
    nechet = [[s[x][0],s[x][1]] for x in range(len(s)) if s[x][1] % 2 != 0]
    k = int(len(chet) * 0.7)
    k1 = int(len(nechet) * 0.25)
    chet = sorted(chet,key=lambda x:x[0])
    chet = [x[0] for x in chet]
    chet1 = chet[:k]
    chet2 = chet[k:]
    nechet = sorted(nechet,key=lambda x:-x[0])
    nechet = [x[0] for x in nechet]
    nechet1 = nechet[:k1]
    nechet2 = nechet[k1:]
    return int(sum(chet1)*0.7)+int(sum(chet2)*0.8)+int(sum(nechet1)*0.85)+sum(nechet2),abs((sum(chet)-(int(sum(chet1)*0.7)+int(sum(chet2)*0.8))) - (sum(nechet) - (int(sum(nechet1)*0.85)+sum(nechet2))))



print(f("26test.txt"))
print("!!!!!!!!!")
print(f("26.txt"))