for x in "0123456789abcdef":
     s1 = f"57a{x}9"
     s2 = f"54{x}"
     s = int(s1, 16) * int(s2, 8)
     if sum(map(int,str(s)))== 40:
         print(x,s)
