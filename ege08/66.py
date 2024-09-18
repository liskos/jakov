import itertools
b = set()
a = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26]
for i in itertools.product(a,repeat = 4):
    if i == i[::-1]:
        b.add(i)
print(len(b),b)
