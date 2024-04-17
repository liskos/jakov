for x in "0123456789abcdef":
     s1 = f"10{x}a"
     s2 = f"ff{x}78"
     s = int(s1, 16) + int(s2, 16)
     if s  % 19 == 0:
         print(x,s // 19)
