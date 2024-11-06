a = [x for x in open("17data/17-362.txt")]
r = []




for i in range(len(a)-1):
    if abs(int(max(str(a[i])))-(int(max(str(a[i+1]))))) < 3:
        r.append(a[i]+a[i+1])


print(len(r),max(r))