for x in "0123456789abcdef":
     s1 = f"8569{x}"
     s2 = f"12{x}48"
     s = int(s1, 16) + int(s2, 16)
     if s % 13 == 0:
         print(x,s // 13)
