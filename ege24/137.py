s = open("24data/24-s1.txt").readlines()

k = 0
for line in s:
    if line.count('J') > line.count('E'):
        k += 1

print(k)
