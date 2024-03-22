for x in "0123456789abcdefgh":
    s1 = f"973f8{x}24"
    s2 = f'7241{x}1E5'
    s3 = f'31{x}154C'
    s = int(s1,18) + int(s2,18) + int(s3,18)
    if s % 11 == 0:
        print(x,s//11)