a = [int(x) for x in open("17data/17-8.txt")]
r = []

for i in range(len(a)-1):
    if (sum((map(int,str(a[i])))) % 2 != 0 and sum(map(int,str(a[i])))) > 5 or (sum(map(int,str(a[i+1]))) % 2 != 0 and sum(map(int,str(a[i+1]))) > 5):
        r.append(a[i] + a[i+1])

print(len(r),max(r))