for x in "0123456789abcdefg":
     s1 = f"10{x}0"
     s2 = f"f0{x}ff"
     s = int(s1, 17) + int(s2, 17)
     if s  % 13 == 0:
         print(x,s // 13)
