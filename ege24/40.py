s = open("24data/k7-m2.txt").read()

s = s.replace("A"," ").replace("B"," ")

print(max(map(len,s.split())),len(s.split()))

