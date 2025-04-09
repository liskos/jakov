for x in "0123456789abcdefghijk":
    s1 = f"82934{x}2"
    s2 = f"2924{x}{x}7"
    s3 = f"67564{x}8"
    s = int(s1,21) + int(s2,21) + int(s3,21)
    if s % 20 == 0:
        print(x,s//20)

