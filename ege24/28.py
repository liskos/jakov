s = open("24data/k7b-2.txt").read()

s = s.replace("E"," ").replace("F"," ")

print(max(map(len,s.split())))