def f(s):
    while ("00" not in s):
        s = s.replace("02","101",1)
        s = s.replace("11","2",1)
        s = s.replace("12","21",1)
        s = s.replace("010","00",1)
    return s
for i in range(120,200):
  s = "0" + "1" * i + "2"  * i  + "0"
  print(len(s),i,sum(map(int,f(s))))