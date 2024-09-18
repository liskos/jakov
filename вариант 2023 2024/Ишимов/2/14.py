for x in '0123456789ABCDEFGHIJ':
   for y in '0123456789ABCDEFGHIJ':
       s = int(f'5{y}4{x}{y}4HJ4', 20) + int(f'4{y}6B{y}{x}1', 20)
       if s % 15 != 0:
           break
   else:
       y = 8
       s = int(f'5{y}4{x}{y}4HJ4', 20) + int(f'4{y}6B{y}{x}1', 20)
       print(x, s,y)