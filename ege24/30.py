s = open("24data/k7b-4.txt").read()

s = s.replace("D"," ").replace("A"," ")

print(max(map(len,s.split())))