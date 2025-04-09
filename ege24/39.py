s = open("24data/k7-m1.txt").read()

s = s.replace("A"," ").replace("B"," ")

print(min(map(len,s.split())),len(s.split()))