s = open("24data/k7b-6.txt").read()

s = s.replace("B"," ").replace("C"," ").replace("E"," ")

print(max(map(len,s.split())))