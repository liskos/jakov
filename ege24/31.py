s = open("24data/k7b-5.txt").read()

s = s.replace("B"," ").replace("D"," ").replace("D"," ").replace("E"," ").replace("F"," ")

print(max(map(len,s.split())))