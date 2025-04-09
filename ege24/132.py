s = open("24data/24-j1.txt").read()

s = s.replace("КОТ","B")
s = s.replace("К","О").replace("Т","О")

print(max(map(len,s.split("О"))))