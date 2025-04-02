s = open("24data/k7a-6.txt").read()

s = s.replace("A"," ").replace("E"," ")

print(max(map(len,s.split())))