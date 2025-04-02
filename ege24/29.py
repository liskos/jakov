s = open("24data/k7b-3.txt").read()

s = s.replace("C"," ").replace("D"," ")

print(max(map(len,s.split())))