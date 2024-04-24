for x in "0123456789abcdef":
     s1 = f"8569{x}"
     s2 = f"12{x}48"
     s = int(s1, 16) + int(s2, 16)
     s = oct(s)[2:]
     if s.count('0') + s.count('2') + s.count('4') + s.count('6') <= 2:
         print(x,s)

