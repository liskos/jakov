s = open("24data/k7a-5.txt").read()

s = s.replace("C"," ").replace("F"," ")

print(max(map(len,s.split())))