a = [int(x) for x in open("17_17558.txt")]
r = []
b = [x for x in a if abs(x) % 32 == 0]







for i in range(len(a)-1):
    if ((a[i] < 0) or (a[i+1] < 0)) and a[i] + a[i+1] < len(b):
        r.append(a[i]+a[i+1])


print(len(r),max(r))