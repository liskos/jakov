s = open("24data/k7-42.txt").read()
i = 1
while "C" * i in s:
    i += 1

print(i-1)