file = open("26data/26-156.txt")
n = int(file.readline())
stoim = list(map(int,file.readline().split()))
print("число человек" , n)
print("стоимость баллов", stoim)
b = []
for i in range(n):
    a = list(map(int,file.readline().split()))
    id = a[0]
    a = a[1:]
    s = 0
    s_shtraf = 0
    k_propusk = 0
    for x in range(10):
        if a[x] < 0:
            s_shtraf += stoim[x]
        elif a[x] == 0:
            k_propusk += 1
        s += a[x] * stoim[x]
    b.append([id,s,s_shtraf,k_propusk])

b = sorted(b,key=lambda x:(-x[1],x[2],x[3],x[0]))
print(*b, sep="\n")
pobeda = b[:1992]
print("последний в 20%", pobeda[-1])
ne_pobeda = b[1992:]
for id,a1,a2,a3 in ne_pobeda:
    if a1 == pobeda[-1][1] and a2 == pobeda[-1][2] and a3 == pobeda[-1][3]:
        pobeda.append([id,a1,a2,a3])

print(len(pobeda))
ne_pobeda = b[len(pobeda):]
ych_vektorini = [x for x in ne_pobeda if x[1] > 0]
print(ych_vektorini)
print("количество возможных участников викторины", len(ych_vektorini))
kk = len(ych_vektorini) // 10
ych_vektorini = ych_vektorini[:kk]
print("ответ 1:",ych_vektorini[1][0])
ans2 = sum([x[1] for x in ych_vektorini])
print(ans2)
