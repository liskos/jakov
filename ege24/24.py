s = open("24data/k7a-4.txt").read()
s = s.replace("D"," ")

print(max(map(len,s.split())))
