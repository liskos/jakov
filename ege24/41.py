s = open("24data/k7-m3.txt").read()

s = s.replace("A"," ").replace("B"," ")

s = s.split()
print(s)
s = [x[0] + x[1:].replace("C","c") for x in s if len(x) < 5]

print(s)