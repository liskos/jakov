# def f(x):
#         k = 0
#         if x % 2 == 0:
#                 k += 1
#         if x % 3 == 0:
#                 k += 1
#         if x % 5 == 0:
#                 k += 1
#         if x % 7 == 0:
#                 k += 1
#         return k
a = [int(x) for x in open("17data/17-4.txt")]
r = []
for i in range(len(a)):
        if sum(1 for x in [2,3,5,7] if a[i] % x == 0)==2:
           r.append(a[i])
print(len(r),max(r)+min(r))