# def delitel(n):
#     a = set()
#     b = []
#     for i in range(1,int(n**0.5)+1):
#         if n % i == 0:
#             b.append(n//i)
#             if max(b) - min(b) > 5000 and n % 1235 == 0:
#                          print(max(b)-min(b))
#                          a.add(i)
#                          a.add(max(b) - min(b))
#     return sorted(a)
def delitel(n):
    a = set()
    for i in range(1,int(n**0.5)+1):
        if n % i == 0:
            if i != n and i != 1:
                a.add(i)
                a.add(n//i)
            else:
                k = 1
    return a

for n in range(1533880,1000000,-1):
    d = delitel(n)
    if len(d) > 2:
         if max(d) - min(d) > 5000 and (max(d) - min(d)) % 1235 == 0:
                print(n,max(d)-min(d))


