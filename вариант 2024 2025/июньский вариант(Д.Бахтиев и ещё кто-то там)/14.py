for x in "0123456789abcdefg":
    s1 = int(f"4b3{x}1c7",14)
    s2 = int(f"5{x}g83f7",17)
    s = s1 + s2
    if s % 15 == 0:
        print(x,s/15)