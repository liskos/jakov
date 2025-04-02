s = open("24data/k7a-2.txt").read()
i = 1
s = s.replace("B"," ").replace("E"," ").replace("F"," ")
print(max(map(len,s.split())))