s = open("24data/24-s1.txt").readlines()

k = 0
for lines in s:
    if lines.count("YZ") > 1:
        k += 1

print(k)
