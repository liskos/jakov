s = open("24data/k7a-1.txt").read()

s = s.replace("D"," ").replace("E"," ")

print(max(map(len, s.split())))