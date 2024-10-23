a = [int(x) for x in open("17data/17-1.txt")]
r = []
for i in range(len(a)-1):
    if ((str(abs(a[i])))[-1] == "6" and a[i] % 3 == 0) or (a[i+1] % 3 == 0 and str(abs(a[i+1]))[-1] == "6"):
        r.append(min(a[i],a[i+1]))
print(len(r),min(r))


# #a = [int(x) for x in open("17data/17-1.txt")]
# r = []
# for i in range(len(a)-1):
#     if (a[i] % 7 == 0 and a[i+1] % 17 != 0 )or (a[i] % 17 != 0 and a[i+1] % 7 == 0):
#      r.append(a[i] + a[i+1])
# print(len(r),min(r))