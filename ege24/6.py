s = open("24data/k7-29.txt").read()
i = 1
while "С" * i in s:
    i += 1


print(i-1)