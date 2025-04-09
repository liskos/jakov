s = open("24data/k7-m4.txt").read()

p = 0
s = s.replace("A"," ").replace("B"," ")

s = s.split()

for i in range(len(s)):
    p += 1
    if len(s[-i]) > 5:
        print(p,len(s),s[-i].replace("C","c"))